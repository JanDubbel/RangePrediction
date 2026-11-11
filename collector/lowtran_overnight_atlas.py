#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resumable patched-geometry LOWTRAN 7 atlas, Python >=3.10, NumPy >=2.0.

Safety: no atmospheric batch runs without --full or --smoke.
Plan: python lowtran_overnight_atlas.py --plan
Preflight: python lowtran_overnight_atlas.py --preflight
Smoke: python lowtran_overnight_atlas.py --smoke
Full (user-triggered only): python lowtran_overnight_atlas.py --full
Resume: run the same --full command again in the same output directory.

Results: SQLite database (with full spectra and components), CSV (integrals), ZIP.
Designed for the component-enabled lowtran7_components_python.zip package.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import itertools
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import time
import traceback
import zipfile

SCRIPT_VERSION = "2026-11-11-atlas-v2-stable-beta"
PATCH_MARKER = "Numerically stable central angle from the chord length."
WAVELENGTH_RANGE = (3.0, 5.0)  # um
STEP_CM = 20                    # cm^-1, native LOWTRAN 7 resolution
BACKGROUND_TEMPS = (250.0, 283.0, 300.0, 320.0)
PROFILES = (1, 2, 3, 4, 5, 6)
VIS_CORE = (5, 10, 15, 20, 30, 50)  # km
VIS_INTERP = (7, 12, 25, 40)        # km
HORIZONTAL = tuple((h, h) for h in (0, .25, .5, 1, 2, 3, 5))
SLANT = ((0, .5), (0, 1), (0, 2), (0, 3), (0, 5),
         (.5, 2), (1, 3), (1, 5), (2, 5), (3, 5))
GEOMETRIES = HORIZONTAL + SLANT
EXTRA_GEOMETRIES = ((0, .25), (0, 4), (.25, 1), (.5, 1), (.5, 3),
                    (1, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5))
DISTANCES = (.5, .75, 1, 1.5, 2, 2.5, 3, 4, 5, 7.5,
             10, 12.5, 15, 20, 25, 30, 40, 60, 80)
OUTPUT_DEFAULT = "lowtran_atlas_corrected_v2"
SMOKE_OUTPUT_DEFAULT = "lowtran_atlas_corrected_smoke"
EXTRA_SHORT_DISTANCES = (1.25, 1.75, 2.25, 2.75, 3.25, 3.5, 4.5)
CSV_NAME = "lowtran_integrals.csv"
DB_NAME = "lowtran_atlas.sqlite"
ARCHIVE_NAME = "lowtran_atlas_bundle.zip"


def task_key(t):
    return "p{profile}_a{aerosol}_v{visibility:g}_h{h1:g}-{h2:g}_d{distance:g}".format(**t)


def valid_distance(h1, h2, distance):
    # Avoid exact/near vertical slant geometries: LOWTRAN 7 can hang on them.
    delta = abs(h2 - h1)
    return distance > delta * 1.05 + 1e-6


def make_tasks(smoke=False, dense_short=False):
    if smoke:
        cases = [(2, 1, 30, 0, 1, 2), (2, 1, 30, 0, 1, 2.5),
                 (2, 1, 30, 0, 1, 3), (2, 1, 30, 0, 1, 4),
                 (2, 1, 30, 0, 0, 20), (3, 1, 30, 0, 0, 20),
                 (2, 1, 30, 0, 3, 20), (3, 4, 10, 1, 3, 10),
                 (5, 5, 30, 5, 5, .5)]
        return [dict(stage=0, profile=p, aerosol=a, visibility=v,
                     h1=h1, h2=h2, distance=d) for p, a, v, h1, h2, d in cases]

    # Ordered stages: a useful, complete first atlas before adding refinements.
    stages = (
        (1, (1,), VIS_CORE, GEOMETRIES),          # Rural, all climates
        (2, (4, 5), VIS_CORE, GEOMETRIES),       # Maritime, urban
        (3, (1, 4, 5), VIS_INTERP, GEOMETRIES), # Intermediate visibilities
        (4, (6,), VIS_CORE, GEOMETRIES),        # Tropospheric aerosol
        (5, (0,), (30,), GEOMETRIES),          # No-aerosol reference (VIS irrelevant)
        (6, (1, 4, 5), VIS_CORE, EXTRA_GEOMETRIES), # More heights and slants
    )
    tasks = []
    for stage, aerosols, visibilities, geometries in stages:
        for p, a, v, (h1, h2), d in itertools.product(
                PROFILES, aerosols, visibilities, geometries, DISTANCES):
            if valid_distance(h1, h2, d):
                tasks.append(dict(stage=stage, profile=p, aerosol=a,
                                  visibility=float(v), h1=float(h1),
                                  h2=float(h2), distance=float(d)))
    if dense_short:
        # Optional supplementary stage: preserve every original task unchanged.
        # Generate extra D values only for geometries where D=5 km was valid;
        # this keeps the new short-range points associated with existing cases.
        for original in list(tasks):
            if original["distance"] != 5.0:
                continue
            for d in EXTRA_SHORT_DISTANCES:
                if valid_distance(original["h1"], original["h2"], d):
                    tasks.append({**original, "stage": 7, "distance": d})
    assert len({task_key(t) for t in tasks}) == len(tasks), "Duplicate tasks!"
    return tasks


def find_package_root(argument):
    """Use the bundled lowtran package in preference to any global installation."""
    here = Path(__file__).resolve().parent
    candidates = []
    if argument:
        candidates.append(Path(argument).resolve())
    candidates.extend((here, here / "lowtran-python", here.parent,
                       here.parent / "lowtran-python", here.parent / "python",
                       here.parent.parent / "python"))
    for root in candidates:
        if (root / "lowtran" / "engineering.py").is_file():
            return root
    raise FileNotFoundError(
        "Cannot find patched lowtran package. Unzip the complete archive "
        "so that lowtran/ is beside this script (or use --package-root PATH)."
    )


def assert_patched_package(root):
    """Refuse to collect data from the previous, geometrically defective core."""
    core_path = root / "lowtran" / "_core.py"
    if not core_path.is_file() or PATCH_MARKER not in core_path.read_text(encoding="utf-8"):
        raise RuntimeError(
            "UNPATCHED/UNKNOWN LOWTRAN CORE: expected stable central-angle "
            "patch in lowtran/_core.py. Do not use the original nightly ZIP."
        )
    if not (root / "lowtran" / "_tables.bin").is_file():
        raise RuntimeError("lowtran/_tables.bin is missing")


def package_fingerprint(root):
    h = hashlib.sha256()
    for name in ("_core.py", "_api.py", "engineering.py", "components.py", "_tables.bin"):
        path = root / "lowtran" / name
        if path.is_file():
            h.update(name.encode())
            h.update(path.read_bytes())
    return h.hexdigest()


def config_fingerprint(package_hash, smoke):
    config = {"version": SCRIPT_VERSION, "package_hash": package_hash,
              "band_um": WAVELENGTH_RANGE, "step_cm": STEP_CM,
              "temperatures_k": BACKGROUND_TEMPS, "smoke": smoke}
    return hashlib.sha256(json.dumps(config, sort_keys=True).encode()).hexdigest()


def connect(db_path):
    conn = sqlite3.connect(str(db_path), timeout=30)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=30000")
    conn.execute("PRAGMA synchronous=NORMAL")
    return conn


def create_schema(conn, fingerprint, root, smoke):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS samples (
      task_key TEXT PRIMARY KEY, stage INTEGER NOT NULL,
      profile INTEGER NOT NULL, aerosol INTEGER NOT NULL,
      visibility_km REAL NOT NULL, h1_km REAL NOT NULL,
      h2_km REAL NOT NULL, distance_km REAL NOT NULL,
      tau_250k REAL NOT NULL, tau_283k REAL NOT NULL,
      tau_300k REAL NOT NULL, tau_320k REAL NOT NULL,
      tau_283k_photon REAL NOT NULL, tau_283k_over_lambda REAL NOT NULL,
      n_wavelengths INTEGER NOT NULL, component_closure_error REAL,
      spectrum_npz BLOB NOT NULL,
      computed_utc TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS failures (
      task_key TEXT PRIMARY KEY, stage INTEGER NOT NULL,
      message TEXT NOT NULL, updated_utc TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX IF NOT EXISTS idx_samples_pavh ON
        samples(profile,aerosol,visibility_km,h1_km,h2_km,distance_km);
    """)
    old = conn.execute("SELECT value FROM meta WHERE key='fingerprint'").fetchone()
    if old and old[0] != fingerprint:
        raise RuntimeError(
            "This output directory contains results from a different model/configuration. "
            "Use a NEW --output directory. Data from different calculations must not mix."
        )
    metadata = {"fingerprint":fingerprint, "script_version":SCRIPT_VERSION,
                "lowtran_package_hash":package_fingerprint(root),
                "run_mode":"smoke" if smoke else "full",
                "wavelength_range_um":str(WAVELENGTH_RANGE),
                "step_cm":str(STEP_CM),
                "band_weight_temperature_k":str(BACKGROUND_TEMPS),
                "geometry_patch":"stable central angle BETA via double-precision asin(chord), "
                                 "experimental LOWTRAN 7 local patch",
                "dataset_provenance":"new independent dataset, not a continuation of original v1",
                "weight_definition":"energy M_lambda; photon lambda*M_lambda; "
                                    "inverse M_lambda/lambda; detector S(lambda)=1",
                "distance_definition":"optical slant length (km), not horizontal projection",
                "season":"0 = automatic; determined from atmospheric MODEL",
                "aerosols":"IHAZE 1 rural, 4 maritime, 5 urban, "
                           "6 tropospheric, 0 disabled; IHAZE 2 omitted because it "
                           "equals IHAZE 1 when VIS is explicitly supplied"}
    conn.executemany("INSERT OR IGNORE INTO meta (key,value) VALUES (?,?)", metadata.items())
    conn.commit()


def get_keys(conn):
    done = {r[0] for r in conn.execute("SELECT task_key FROM samples")}
    failed = {r[0] for r in conn.execute("SELECT task_key FROM failures")}
    return done, failed


def mark_active(conn, key):
    now = time.time()
    conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('active_task',?)", (key,))
    conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('worker_tick',?)", (str(now),))
    conn.commit()


def mark_idle(conn):
    conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('active_task','')")
    conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('worker_tick',?)",(str(time.time()),))
    conn.commit()


def mark_failure(conn, t, msg):
    conn.execute("INSERT OR REPLACE INTO failures(task_key,stage,message) VALUES (?,?,?)",
                 (task_key(t), t["stage"], str(msg)[:3000]))
    conn.commit()


def planck(wl_um, t_k, np):
    return 1.0 / (wl_um ** 5 * np.expm1(14387.768775039337 / (wl_um * t_k)))


def integrate(lam, tau, temp_k, np, power=0):
    # Spectrum is wavenumber-uniform; integrate in wavelength, not sample index.
    # Endpoint interpolation avoids integration bias from LOWTRAN grid snapping.
    low, high = WAVELENGTH_RANGE
    if lam[0] > low + 1e-5 or lam[-1] < high - 1e-5:
        raise ValueError(f"Spectrum does not bracket [{low}, {high}] um: "
                         f"[{lam[0]:.6f}, {lam[-1]:.6f}]")
    interior = (lam > low) & (lam < high)
    x = np.r_[low, lam[interior], high]
    y = np.r_[np.interp(low, lam, tau), tau[interior], np.interp(high, lam, tau)]
    weights = planck(x, temp_k, np) * x ** power
    trapz = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    return float(trapz(weights * y, x) / trapz(weights, x))


def compute_sample(t, Atmosphere, np):
    atmosphere = Atmosphere(profile=t["profile"], aerosol=t["aerosol"],
                            visibility_km=t["visibility"], season=0)
    args = dict(distance_km=t["distance"], altitude_start_km=t["h1"],
                altitude_end_km=t["h2"], wavelength_range=WAVELENGTH_RANGE,
                step_cm=STEP_CM)
    if hasattr(atmosphere, "spectrum_components"):
        result = atmosphere.spectrum_components(**args).sorted()
        tau = np.asarray(result.total, dtype=np.float64)
        wl = np.asarray(result.wavelength_um, dtype=np.float64)
        comp = {name: np.asarray(vec, dtype="<f4") for name, vec in result.components.items()}
        comp["h2o_total"] = np.asarray(result.h2o, dtype="<f4")
        comp["other_gases"] = np.asarray(result.other_gases, dtype="<f4")
        closure = float(result.closure_error)
        if closure > 3e-5:
            raise ValueError(f"LOWTRAN component closure error {closure:.4g}")
    else:
        result = atmosphere.spectrum(**args)
        ix = np.argsort(result.wavelength_um)
        tau = np.asarray(result.transmission, dtype=np.float64)[ix]
        wl = np.asarray(result.wavelength_um, dtype=np.float64)[ix]
        comp = {}
        closure = None
    if len(wl) < 10 or not np.isfinite(wl).all() or not np.isfinite(tau).all():
        raise ValueError("Invalid/empty spectrum")
    if not np.all(np.diff(wl) > 0):
        raise ValueError("Non-increasing wavelength grid")
    if float(tau.min()) < -1e-4 or float(tau.max()) > 1.0001:
        raise ValueError("Unphysical spectral transmittance outside [0,1]")

    values = {f"tau_{int(T)}k":integrate(wl,tau,T,np) for T in BACKGROUND_TEMPS}
    values["tau_283k_photon"] = integrate(wl,tau,283,np,power=1)
    values["tau_283k_over_lambda"] = integrate(wl,tau,283,np,power=-1)
    for name, value in values.items():
        if not 0 <= value <= 1.00001:
            raise ValueError(f"Invalid {name}: {value}")
    # Compressed 1-D arrays inside an NPZ, stored as one SQLite BLOB per case.
    # This preserves raw LOWTRAN spectra for future reweighting / other detectors.
    buf = io.BytesIO()
    np.savez_compressed(buf,
        wavelength_um=wl.astype("<f4"),
        total=tau.astype("<f4"), **comp)
    values.update(n_wavelengths=len(wl), component_closure_error=closure,
                  spectrum_npz=buf.getvalue())
    return values


def worker_main(args):
    root = find_package_root(args.package_root)
    sys.path.insert(0, str(root))
    import numpy as np
    from lowtran import Atmosphere

    db_path = Path(args.db)
    with Path(args.batch_file).open(encoding="utf-8") as f:
        batch = json.load(f)
    con = connect(db_path)
    done, failed = get_keys(con)
    cols = ("task_key", "stage", "profile", "aerosol", "visibility_km",
            "h1_km", "h2_km", "distance_km", "tau_250k", "tau_283k",
            "tau_300k", "tau_320k", "tau_283k_photon",
            "tau_283k_over_lambda", "n_wavelengths",
            "component_closure_error", "spectrum_npz")
    sql = "INSERT OR REPLACE INTO samples (" + ",".join(cols) + ") VALUES (" + ",".join("?" for _ in cols) + ")"
    for t in batch:
        key = task_key(t)
        if key in done or key in failed:
            continue
        mark_active(con, key)
        try:
            vals = compute_sample(t, Atmosphere, np)
            record = (key, t["stage"], t["profile"], t["aerosol"], t["visibility"],
                      t["h1"], t["h2"], t["distance"],
                      *(vals[name] for name in cols[8:]))
            con.execute(sql, record)
            con.commit()
        except Exception:
            message = traceback.format_exc(limit=7)
            mark_failure(con,t,message)
            print(f"FAILED {key}: {message[-550:]}", flush=True)
        mark_idle(con)
    mark_idle(con)
    con.close()
    return 0


def do_export(output_dir, con, total_tasks=None):
    csv_path = output_dir / CSV_NAME
    cols = ("task_key", "stage", "profile", "aerosol", "visibility_km",
            "h1_km", "h2_km", "distance_km", "tau_250k", "tau_283k",
            "tau_300k", "tau_320k", "tau_283k_photon",
            "tau_283k_over_lambda", "n_wavelengths",
            "component_closure_error", "computed_utc")
    tmp_csv = csv_path.with_suffix(".csv.tmp")
    with tmp_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(cols)
        query = "SELECT " + ",".join(cols) + " FROM samples ORDER BY stage,profile,aerosol,visibility_km,h1_km,h2_km,distance_km"
        w.writerows(con.execute(query))
    tmp_csv.replace(csv_path)
    count = con.execute("SELECT COUNT(*) FROM samples").fetchone()[0]
    nfail = con.execute("SELECT COUNT(*) FROM failures").fetchone()[0]
    stage_counts = dict(con.execute("SELECT stage,COUNT(*) FROM samples GROUP BY stage ORDER BY stage"))
    meta = dict(con.execute("SELECT key,value FROM meta WHERE key != 'active_task' AND key != 'worker_tick'"))
    manifest = {"total_samples":count,"failed_samples":nfail,
                "planned_samples":total_tasks,"counts_by_stage":stage_counts,
                "metadata":meta,"created_utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())}
    mf_path = output_dir / "manifest.json"
    mf_path.write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding="utf-8")

    # Consistent, checkpointed database copy (no loose SQLite WAL files needed).
    snap = output_dir / "_snapshot_for_zip.sqlite"
    try:
        snap.unlink(missing_ok=True)
    except PermissionError as exc:
        raise RuntimeError(
            "Old SQLite export snapshot is still locked. Close programs that "
            "read _snapshot_for_zip.sqlite, then retry --export-only"
        ) from exc
    backup = sqlite3.connect(str(snap))
    try:
        con.backup(backup)
    finally:
        # sqlite3.Connection context manager does NOT close the file handle.
        # Explicit close prevents WinError 32 on Windows when deleting snapshot.
        backup.close()
    archive = output_dir / ARCHIVE_NAME
    tmp_archive = archive.with_suffix(".zip.tmp")
    with zipfile.ZipFile(tmp_archive,"w",compression=zipfile.ZIP_DEFLATED,
                         compresslevel=5,allowZip64=True) as zf:
        zf.write(csv_path,CSV_NAME)
        zf.write(mf_path,"manifest.json")
        zf.write(snap,DB_NAME)
        for name in ("lowtran_overnight_atlas.py","README_NIGHTLY.txt"):
            p = Path(__file__).resolve().parent / name
            if p.exists():
                zf.write(p,name)
    tmp_archive.replace(archive)
    try:
        snap.unlink(missing_ok=True)
    except PermissionError:
        # ZIP is already atomically finalized; do not report the entire run
        # as failed because antivirus/Windows has briefly locked the snapshot.
        print("WARNING: Could not remove temporary SQLite snapshot; "
              "the finished ZIP is valid. Remove the snapshot later.", flush=True)
    print(f"Export: {count} samples; {nfail} errors. Stages: {stage_counts}",flush=True)
    print(f"CSV: {csv_path}\nSQLite: {output_dir / DB_NAME}\nZIP: {archive}",flush=True)


def run_preflight(root):
    """Validate the corrected 2.5-3 km geometry on the installed core."""
    assert_patched_package(root)
    sys.path.insert(0, str(root))
    import numpy as np
    from lowtran import Atmosphere
    reference = ((2.0, 0.4015086), (2.5, 0.3624481),
                 (3.0, 0.3303447), (4.0, 0.2803442))
    measured = []
    for d, expected in reference:
        t = dict(stage=0, profile=2, aerosol=1, visibility=30.0,
                 h1=0.0, h2=1.0, distance=d)
        tau = compute_sample(t, Atmosphere, np)["tau_283k"]
        print(f"PRECHECK | 0 -> 1 km | D={d:4.1f} km | tau(283 K)={tau:.8f}",flush=True)
        if abs(tau-expected) > 0.002:
            raise RuntimeError(
                f"Patched LOWTRAN regression FAILED at D={d:g} km: "
                f"tau={tau:.6f}, expected about {expected:.6f}"
            )
        measured.append(tau)
    if not all(a > b for a,b in zip(measured,measured[1:])):
        raise RuntimeError("NON-MONOTONIC patched short slant test")
    print("PRECHECK OK: patched short slant is monotonic and agrees "
          "with reference within 0.002",flush=True)


def show_status(path):
    db = path / DB_NAME
    if not db.is_file():
        print(f"No atlas database yet: {db}")
        return
    con = sqlite3.connect(str(db),timeout=30)
    try:
        meta = dict(con.execute("SELECT key,value FROM meta"))
        done = con.execute("SELECT COUNT(*) FROM samples").fetchone()[0]
        failed = con.execute("SELECT COUNT(*) FROM failures").fetchone()[0]
        stages = dict(con.execute("SELECT stage,COUNT(*) FROM samples GROUP BY stage"))
        print(f"Status: {path} | done={done:,} | failed={failed:,}")
        print(f"Stages: {stages} | script={meta.get('script_version')}")
        print(f"Patch: {meta.get('geometry_patch', '<NOT DOCUMENTED>')}")
    finally:
        con.close()


def main():
    p = argparse.ArgumentParser(description="LOWTRAN 7 overnight atlas, resumable, full spectra")
    p.add_argument("--full",action="store_true",help="EXPLICITLY start the complete overnight calculation")
    p.add_argument("--plan",action="store_true",help="Show tasks without running simulations")
    p.add_argument("--preflight",action="store_true",help="Check patched geometry, without writing a database")
    p.add_argument("--status",action="store_true",help="Print progress without running simulations")
    p.add_argument("--dense-short",action="store_true",help="Add an optional supplemental stage for D=1.25..4.5 km")
    p.add_argument("--hours",type=float,default=11.5,help="Maximum wall-clock hours for this invocation (default: 11.5)")
    p.add_argument("--output",type=Path,default=None,help="New output folder, reused to resume")
    p.add_argument("--package-root",type=str,default=None,help="Folder containing the lowtran/ Python package")
    p.add_argument("--smoke",action="store_true",help="Nine lightweight test cases only (separate output)")
    p.add_argument("--export-only",action="store_true",help="Rebuild CSV and ZIP from existing SQLite database")
    p.add_argument("--retry-errors",action="store_true",help="Clear logged errors and retry them")
    p.add_argument("--batch",type=int,default=40,help="Calculations per isolated worker process (default:40)")
    p.add_argument("--case-timeout",type=float,default=75.0,help="Kill stalled worker after this many seconds without progress")
    p.add_argument("--internal-worker",action="store_true",help=argparse.SUPPRESS)
    p.add_argument("--db",type=str,default=None,help=argparse.SUPPRESS)
    p.add_argument("--batch-file",type=str,default=None,help=argparse.SUPPRESS)
    args = p.parse_args()
    if args.internal_worker:
        return worker_main(args)
    if args.hours <= 0 or args.case_timeout < 10 or args.batch < 1:
        p.error("--hours > 0, --case-timeout >= 10, --batch >=1 required")
    if args.output is None:
        args.output = Path(SMOKE_OUTPUT_DEFAULT if args.smoke else OUTPUT_DEFAULT)
    if args.plan:
        tasks=make_tasks(args.smoke,args.dense_short)
        from collections import Counter
        print(f"Plan: {len(tasks):,} simulations; by stage {dict(sorted(Counter(t['stage'] for t in tasks).items()))}")
        print(f"Mode: {'smoke' if args.smoke else 'full'} | dense_short={args.dense_short}")
        return 0
    out = args.output.resolve()
    if args.status:
        return show_status(out)
    if not (args.smoke or args.full or args.preflight or args.export_only):
        p.print_help()
        print("\nSAFE DEFAULT: nothing was calculated. Use --smoke first; "
              "use --full only when you explicitly decide to start the night run.")
        return 0
    if args.full and args.smoke:
        p.error("Choose either --full or --smoke, not both")
    root = find_package_root(args.package_root) if not args.export_only else None
    if root is not None:
        assert_patched_package(root)
    if args.preflight:
        run_preflight(root)
        return 0
    out.mkdir(parents=True,exist_ok=True)
    db_path = out / DB_NAME
    if args.export_only:
        if not db_path.is_file():
            raise FileNotFoundError(f"Database not found: {db_path}")
        con = connect(db_path)
        try:
            old_meta = dict(con.execute("SELECT key,value FROM meta"))
            if old_meta.get("script_version") != SCRIPT_VERSION:
                raise RuntimeError("Refusing to export an old/unpatched database; "
                                   "use the original program for old data")
            do_export(out, con)
        finally:
            con.close()
        return 0

    # Import test in the parent BEFORE launching long-running worker processes.
    sys.path.insert(0,str(root))
    import numpy as np
    from lowtran import Atmosphere
    if not hasattr(np,"expm1") or not hasattr(Atmosphere,"spectrum"):
        raise RuntimeError("NumPy/LOWTRAN incompatible; use supplied package")
    # Validate the known historically defective 2.5-3 km slant geometry
    # BEFORE writing to the full database.
    run_preflight(root)
    package_hash = package_fingerprint(root)
    fingerprint = config_fingerprint(package_hash,args.smoke)
    con = connect(db_path)
    create_schema(con,fingerprint,root,args.smoke)
    # Additional short-range points can be appended on a later invocation;
    # the model fingerprint remains the same because the physics is unchanged.
    con.execute("INSERT OR REPLACE INTO meta(key,value) VALUES (?,?)",
                ("dense_short_requested", str(bool(args.dense_short))))
    con.commit()
    if args.retry_errors:
        con.execute("DELETE FROM failures")
        con.commit()

    tasks = make_tasks(args.smoke,args.dense_short)
    done, failed = get_keys(con)
    pending = [t for t in tasks if task_key(t) not in done and task_key(t) not in failed]
    print(f"LOWTRAN ATLAS v2 [STABLE BETA PATCH] | grid {STEP_CM} cm^-1 | band 3-5 um",flush=True)
    print(f"Package: {root} | SHA256 {package_hash[:16]} | components: {hasattr(Atmosphere,'spectrum_components')}",flush=True)
    print(f"Planned {len(tasks):,} points | already done {len(done):,} | errors {len(failed)} | remaining {len(pending):,}",flush=True)
    print(f"Run limit {args.hours:g} h | output {out}",flush=True)
    start=time.monotonic()
    deadline=start + args.hours*3600
    progress_last=time.monotonic()
    batches=0
    worker_log=out/"worker_errors.log"
    batch_path=out/"_worker_batch.json"
    try:
        while pending and time.monotonic() < deadline-5:
            batch=pending[:args.batch]
            del pending[:len(batch)]
            batch_path.write_text(json.dumps(batch),encoding="utf-8")
            cmd=[sys.executable,str(Path(__file__).resolve()),"--internal-worker",
                 "--db",str(db_path),"--batch-file",str(batch_path),
                 "--package-root",str(root)]
            reason=""
            with worker_log.open("a",encoding="utf-8") as logfile:
                child=subprocess.Popen(cmd,stdout=logfile,stderr=subprocess.STDOUT)
                last_tick = time.time()
                # Independent parent watchdog: safe on Linux and Windows.
                while child.poll() is None:
                    time.sleep(.7)
                    try:
                        r=con.execute("SELECT value FROM meta WHERE key='worker_tick'").fetchone()
                        if r:
                            last_tick=max(last_tick,float(r[0]))
                    except sqlite3.OperationalError:
                        pass
                    if time.monotonic() >= deadline:
                        reason="time limit reached"
                        child.kill();break
                    if time.time()-last_tick > args.case_timeout:
                        reason="worker stalled; timed out"
                        child.kill();break
                child.wait()
            batches+=1
            just_done,just_failed=get_keys(con)
            if reason == "worker stalled; timed out":
                active = con.execute("SELECT value FROM meta WHERE key='active_task'").fetchone()
                active_key=active[0] if active else ""
                stuck=next((t for t in batch if task_key(t)==active_key),None)
                if stuck and active_key not in just_done:
                    mark_failure(con,stuck,reason+f" (>{args.case_timeout:g}s)")
                    just_failed.add(active_key)
                    print(f"WATCHDOG: skipped {active_key} after timeout",flush=True)
            remaining_batch=[t for t in batch if task_key(t) not in just_done and task_key(t) not in just_failed]
            if reason == "time limit reached":
                print("Time limit reached; current batch stopped. Saved all completed points.",flush=True)
                break
            if child.returncode !=0 and not reason:
                print(f"Worker exited with code {child.returncode}; read {worker_log}",flush=True)
                # Prevent endless child-restart loops if importing the package fails.
                if len(remaining_batch)==len(batch):
                    raise RuntimeError(f"Worker could not compute any points. Check {worker_log}")
            pending=remaining_batch+pending
            if time.monotonic()-progress_last>25 or args.smoke or batches%10==0:
                done_n=len(just_done)
                fail_n=len(just_failed)
                rate=(done_n-len(done))/max(time.monotonic()-start,1)
                print(f"[{(time.monotonic()-start)/60:.1f} min] DONE {done_n:,}/{len(tasks):,} | "
                      f"failed {fail_n} | speed {rate:.2f} calc/s | "
                      f"last stage {batch[0]['stage']}",flush=True)
                progress_last=time.monotonic()
        do_export(out,con,len(tasks))
        success=con.execute("SELECT COUNT(*) FROM samples").fetchone()[0]
        return 0 if success else 1
    except KeyboardInterrupt:
        print("Interrupted. Exporting completed results...",flush=True)
        do_export(out,con,len(tasks))
        return 130
    finally:
        con.close()
        batch_path.unlink(missing_ok=True)


if __name__=="__main__":
    sys.exit(main())

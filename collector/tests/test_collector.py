"""Fast, offline unit tests for the new atlas collector (no full computation)."""
import importlib.util
from pathlib import Path
import sqlite3
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('collector', ROOT / 'lowtran_overnight_atlas.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class CollectorTests(unittest.TestCase):
    def test_original_task_count_exact(self):
        tasks = mod.make_tasks()
        self.assertEqual(len(tasks), 78618)
        self.assertEqual(len({mod.task_key(t) for t in tasks}), len(tasks))

    def test_dense_short_adds_only_new_tasks(self):
        base = {mod.task_key(t) for t in mod.make_tasks()}
        extended = mod.make_tasks(dense_short=True)
        self.assertEqual(len(extended), 105948)
        self.assertTrue(base.issubset({mod.task_key(t) for t in extended}))
        self.assertEqual(sum(t['stage'] == 7 for t in extended), 27330)

    def test_smoke_cases_include_short_slant(self):
        smoke = mod.make_tasks(smoke=True)
        self.assertEqual(len(smoke), 9)
        self.assertTrue(any(t['h1'] == 0 and t['h2'] == 1 and t['distance'] == 2.5 for t in smoke))

    def test_package_is_patched(self):
        mod.assert_patched_package(mod.find_package_root(None))

    def test_sqlite_mismatch_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            conn = mod.connect(Path(folder) / 'test.sqlite')
            try:
                mod.create_schema(conn, 'new-hash', mod.find_package_root(None), False)
                with self.assertRaises(RuntimeError):
                    mod.create_schema(conn, 'different-hash', mod.find_package_root(None), False)
            finally:
                conn.close()


if __name__ == '__main__':
    unittest.main()

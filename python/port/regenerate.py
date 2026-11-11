"""Optional developer tool. Regenerate the Python port from the upstream Fortran."""
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path, help='path to upstream lowtran7.f')
    parser.add_argument('--compiler', default='gfortran', help='GNU Fortran 14.2 executable')
    args = parser.parse_args()
    scripts = Path(__file__).resolve().parent

    with tempfile.TemporaryDirectory() as directory:
        work = Path(directory)
        with (work / 'port.f').open('w') as out:
            subprocess.run(
                [sys.executable, str(scripts / 'prepare.py'), str(args.source.resolve())],
                stdout=out, check=True,
            )
        subprocess.run(
            [args.compiler, '-std=legacy', '-w', '-g', '-fPIC', '-shared',
             '-fdump-tree-gimple', 'port.f', '-o', 'port.so'],
            cwd=work, check=True,
        )
        subprocess.run(
            [sys.executable, str(scripts / 'translate.py'), str(scripts.parent / 'lowtran')],
            cwd=work, check=True,
        )


if __name__ == '__main__':
    main()

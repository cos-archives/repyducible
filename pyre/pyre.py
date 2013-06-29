"""Pyre makes it easy to package and use reproducible Python environments.

A pyre archive contains all of the information necessary to recreate the
environment in which it was created.

Usage:
    pyre freeze [options]
    pyre -h | --help
    pyre --version

Options:
    -h --help       Show this screen
    --out           The output archive's path; defaults to "archive.pyre".
    --in            The directory to archive; defaults to the current path.

"""
from docopt import docopt

import os


def create_archive(source=None, out='archive.pyre'):
    pass


def run_command(args):
    """Handles the call from the commandline"""

    # default to the current path if necessary
    input_path = args.get('--in') or os.path.abspath(os.path.curdir)

    # default to ./archive.pyre if necessary
    output_path = args.get('--out') or os.path.abspath(
        os.path.join(os.path.curdir, 'archive.pyre')
    )

    print('in: {}'.format(input_path))
    print('out: {}'.format(output_path))

if __name__ == '__main__':
    run_command(docopt(__doc__, version='0.0.1a'))


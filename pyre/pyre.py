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
import shutil
import tempfile
import zipfile

from .config import PyreConfig


def create_archive(source, destination,
                   overwrite=False):
    """Create an archive of a directory


    :param source: The absolute path of the directory to be archived
    :param destination: The absolute path to the archive file to be created
    :return: On success, the path to the archive. On failure, ``None``.
    """
    dir_depth = len(source) + 1

    if not overwrite and os.path.isfile(destination):
        raise IOError('File exists.')

    temp_file, temp_file_name = tempfile.mkstemp()

    with zipfile.ZipFile(temp_file_name, 'w') as archive:
        # add all files in the path
        for base, dirs, files in os.walk(source):
            for f in files:
                file_path = os.path.join(base, f)
                archive.write(file_path, file_path[dir_depth:])

    shutil.move(temp_file_name, destination)
    return destination


def run_command(args=None):
    """Handles the call from the commandline"""

    args = args or {}

    # default to the current path if necessary
    input_path = args.get('--in') or os.path.abspath(os.path.curdir)

    # default to ./archive.pyre if necessary
    output_path = args.get('--out') or os.path.abspath(
        os.path.join(os.path.curdir, 'archive.pyre')
    )

    # create a .pyre_config
    config_file = os.path.join(input_path, '.pyre_config')
    if os.path.isfile(config_file):
        raise IOError('.pyre_config exists!')

    config = PyreConfig(config_file)
    config.save()

    create_archive(source=input_path, destination=output_path)

    os.remove(config_file)

if __name__ == '__main__':
    run_command(docopt(__doc__, version='0.0.1a'))
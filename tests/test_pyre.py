import os
import shutil
import tempfile
import unittest
import zipfile

from pyre import pyre


class PyreExecutableTestCase(unittest.TestCase):

    def setUp(self):
        # create a directory in a temporary location for testing
        try:
            self.path
        except AttributeError:
            self.test_path = os.path.abspath('examples/')
        os.chdir(self.test_path)

    def tearDown(self):
        os.chdir(os.pardir)

    def test_defaults(self):
        os.chdir('simple_environment')

        # run pyre with defaults
        pyre.run_command()

        # Archive was created
        self.assertTrue(os.path.isfile('archive.pyre'))
        self.assertTrue(zipfile.is_zipfile('archive.pyre'))

        self._verify_zip('archive.pyre', os.getcwd())

        os.remove('archive.pyre')
        os.chdir(self.test_path)

    def test_arg_out(self):
        os.chdir('simple_environment')

        # run pyre with a custom output
        pyre.run_command({'--out': 'renamed.pyre'})

        # archive was created
        self.assertTrue(os.path.isfile('renamed.pyre'))

        os.remove('renamed.pyre')
        os.chdir(os.pardir)

    def test_arg_in(self):
        pyre.run_command({'--in': 'simple_environment'})
        self.assertTrue(os.path.isfile('archive.pyre'))
        os.remove('archive.pyre')

    def test_file_exists(self):
        os.chdir('simple_environment')

        with tempfile.NamedTemporaryFile() as archive:
            with self.assertRaises(OSError):
                pyre.run_command({'--out': archive.name})

    def _verify_zip(self, zip_path, source_path):
        archive = zipfile.ZipFile(zip_path)

        # iterate over the files in the archive, make sure they're in the
        # original, and that the .pyre_config exists.
        has_config = False
        files = archive.infolist()
        for f in files:
            if f.filename == '.pyre_config':
                has_config = True
                continue

            self.assertTrue(os.path.isfile(
                os.path.join(source_path, f.filename)
            ))
        self.assertTrue(has_config)
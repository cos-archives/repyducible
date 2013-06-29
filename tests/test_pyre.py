import os
import subprocess
import unittest

from pyre import pyre


class PyreExecutableTestCase(unittest.TestCase):

    def setUp(self):
        # create a directory in a temporary location for testing
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

        os.remove('archive.pyre')
        os.chdir(os.pardir)

    def test_arg_out(self):
        os.chdir('simple_environment')

        # run pyre with a custom output
        pyre.run_command({'--out': 'renamed.pyre'})

        # archive was created
        self.assertTrue(os.path.isfile('renamed.pyre'))

        os.remove('renamed.pyre')
        os.chdir(os.pardir)

from io import StringIO
import unittest
import yaml

from pyre.config import PyreConfig


class PyreConfigTestCase(unittest.TestCase):

    def test_add_package(self):
        conf = PyreConfig()
        conf['packages']['foo'] = '1.2.3'
        self.assertEqual(conf['packages']['foo'], '1.2.3')

    def test_render(self):
        conf = PyreConfig()
        self.assertEqual(
            conf,
            yaml.load(str(conf))
        )

    def test_supplied_version(self):
        conf = PyreConfig(python_version='1.2.3')
        self.assertEqual(conf['python']['version'], '1.2.3')
        self.assertEqual(
            yaml.load(str(conf))['python']['version'],
            '1.2.3'
        )

    def test_save_to_file(self):
        f = StringIO()
        conf = PyreConfig(out=f)
        conf.save()
        self.assertEqual(
            yaml.load(f.getvalue()),
            yaml.load(str(conf)),
        )
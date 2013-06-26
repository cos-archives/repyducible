import unittest
import yaml

from repyducible import PyreConfig


class PyreConfigTestCase(unittest.TestCase):
    def test_add_module(self):
        conf = PyreConfig()
        conf['modules']['foo'] = '1.2.3'
        self.assertEqual(conf['modules']['foo'], '1.2.3')

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
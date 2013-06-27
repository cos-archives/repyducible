from cStringIO import StringIO
import unittest
import yaml

from repyducible.config import PyreConfig


class PyreConfigTestCase(unittest.TestCase):

    TMP_CONF_PATH = tempfile.tempdir

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

    def test_save_to_file(self):
        f = StringIO()
        conf = PyreConfig(path=f)
        conf.save()
        self.assertEqual(
            yaml.load(f.getvalue())

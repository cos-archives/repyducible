import subprocess
import sys
import yaml


class PyreConfig(dict):
    def __init__(self, path=None, modules=None, python_version=None):
        self['modules'] = modules or self._loaded_modules()
        self['python'] = {
            'version': python_version or'{p.major}.{p.minor}.{p.micro}'.format(
                p=sys.version_info
            ),
        }
        self.path = path
        super(PyreConfig, self).__init__()

    def __str__(self):
        return yaml.dump(dict(self))

    def save(self):
        """Save the config to disk

        :return: `None` if a string was passed to the class constructor; a file
                 object if one was provided to the same.
        """
        if isinstance(self.path, basestring):
            with open(self.path, 'w') as f:
                f.write(str(self))
        else:
            self.path.write(str(self))

    def _loaded_modules(self):
        result = subprocess.check_output(['pip', 'freeze']).strip()
        modules = dict()
        for i in [x.split('==') for x in result.split('\n')]:
            modules[i[0]] = str(i[1])
        return modules


def to_yaml(obj):
    yaml.dump(
        obj,
        width=80,
        indent=4,
    )
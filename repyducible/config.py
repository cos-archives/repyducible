import subprocess
import sys
import yaml


class PyreConfig(dict):
    """The config state of the host system."""

    def __init__(self, out=None, packages=None, python_version=None):
        """


        :param out: The path to the config file on disk; or, a file-like object
                    to be returned by the `PyreConfig.save()` method.
        :param packages: A list of packages to include. If not provided, this
                         will be inferred from the current execution
                         environmnet, via pip.
        :param python_version: The specific python version to require. If not
                                provided, it will be inferred from the execution
                                environment.
        """
        self['packages'] = packages or self._installed_packages()
        self['python'] = {
            'version': python_version or'{p.major}.{p.minor}.{p.micro}'.format(
                p=sys.version_info
            ),
        }
        self.out = out
        super(PyreConfig, self).__init__()

    def __str__(self):
        """
        :return: A YAML representation of the configuration option.
        """
        return yaml.dump(dict(self))

    def save(self):
        """Save the config to disk

        :return: `None` if a string was passed to the class constructor; a file
                 object if one was provided to the same.
        """
        if isinstance(self.out, str):
            with open(self.out, 'w') as f:
                f.write(str(self))
        else:
            self.out.write(str(self))

    def _installed_packages(self):
        """Returns a dict of installed packages and their versions.
        """
        result = subprocess.check_output(['pip', 'freeze']).strip()
        packages = dict()
        for i in [x.split('==') for x in str(result).split('\n')]:
            packages[i[0]] = str(i[1])
        return packages


def to_yaml(obj):
    yaml.dump(
        obj,
        width=80,
        indent=4,
    )
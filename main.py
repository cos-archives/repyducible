from optparse import OptionParser
import zipfile
import pip
import yaml
import os

###################################
# Build Phase

def generate_requirements(code):
    # if code is ipython notebook
        # parse ipynb with json
        # extract code types
        # put into one string
        # run pip freeze code on it
        # write requirements.txt
    pass

source_path = 'examples/xkcd.repy'

def build_zip_container(path):
    rootlen = len(path) + 1
    path = path + 'z'
    with zipfile.ZipFile(path, 'w') as zip:
        for base, dirs, files in os.walk(source_path):
            for file in files:
                fn = os.path.join(base, file)
                zip.write(fn, fn[rootlen:])

build_zip_container(source_path)

###################################
# Run Phase

usage = "usage: %prog arg1"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()

args = ['examples/xkcd.repyz'] # For testing purposes

with zipfile.ZipFile(args[0], 'r') as myzip:
    myzip.extractall()

with open(os.path.join(source_path, 'config'), 'r') as f:
    config = yaml.load(f.read())

# This is for the pythonbrew based workflow
    #else curl
# if config['python']['version']
    #else pythonbrew install
# if vemv with name
    # if date
# else create venv re

# if not pythonbrew:
    # curl pythonbrew
# if not python_version in pythonbrew list
print 'pythonbrew use {python_version}'.format(python_version=config['python']['version'])
# if not project_name in pythonbrew venv list and date check
print 'pythonbrew venv create {project_name}'.format(project_name=os.path.split(source_path)[1])
print 'pip install -r {path_to_requirements}'.format(path_to_requirements=os.path.join(source_path, 'requirements.txt'))
# run the following
print 'cd {path}'.format(path=source_path)
print 'ipython notebook'
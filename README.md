Pyre: Python Reproducibility Project
====================================

The goal of this project is to make computation--specifically python (for now)--for reproducible. We'll start with encapsulating--zipping up--ipython notebooks with requirements files, local data, a config file with python version information (for now), ipython notebook profiles, the notebooks themselves, and, eventually, salt-like scripts.

Command Line Player
-------------------
- use pythonbrew and/or bash to create encapusulated python distributions and virtual environments
- pip freeze an ipython notebook

GUI Player
----------
- evaluate py2app vs deep freeze, cx_freeze, etc.
- switch between python versions in py2app

For Later
-----

Salt Lite (working name: low sodium)
------------------------------------
- yaml abstraction

Virtual Machine Spawning
------------------------
- fire up web server for interaction

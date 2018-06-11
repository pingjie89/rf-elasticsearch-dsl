import re
from io import open  # required for Python 2
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

from setuptools import find_packages, setup

CURDIR = dirname(abspath(__file__))

CLASSIFIERS = '''
Development Status :: 2 - Pre-Alpha
License :: OSI Approved :: MIT License
Operating System :: POSIX
Programming Language :: Python
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Topic :: Software Development :: Testing
Topic :: Software Development :: Quality Assurance
Framework :: Robot Framework
Framework :: Robot Framework :: Library
'''.strip().splitlines()

with open(join(CURDIR, 'RobotElasticsearch', 'version.py'), encoding="utf-8") as f:
    VERSION = re.search("__version__ = '(.*)'", f.read()).group(1)
with open(join(CURDIR, 'README.rst'), encoding="utf-8") as f:
    DESCRIPTION = f.read()
with open(join(CURDIR, 'requirements.txt'), encoding="utf-8") as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name             = 'rf-elasticsearch-dsl',
    version          = VERSION,
    description      = 'Robot Framework keyword library for python elasticsearch-dsl library',
    long_description = DESCRIPTION,
    author           = 'Ng Ping Jie',
    author_email     = 'pingjie.ng@outlook.com',
    url              = 'https://github.com/pingjie89/rf-elasticsearch-dsl',
    license          = 'MIT License',
    keywords         = 'robotframework test library elasticsearch elasticsearch_dsl',
    classifiers      = CLASSIFIERS,
    install_requires = REQUIREMENTS,
    packages         = ['RobotElasticsearch']
)
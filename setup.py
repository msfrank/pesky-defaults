#!/usr/bin/env python

from setuptools import setup

# jump through some hoops to get access to versionstring()
from sys import path
from os.path import abspath, dirname
path.insert(0, abspath(dirname(__file__)))
from pesky.defaults import versionstring

setup(
    # package description
    name = "pesky-defaults",
    version = versionstring(),
    description="Pesky configuration defaults interface",
    author="Michael Frank",
    author_email="msfrank@syntaxockey.com",
    # installation dependencies
    install_requires=[
        ],
    # package classifiers for PyPI
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License", 
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        ],
    # package contents
    namespace_packages=[
        "pesky",
        ],
    packages=[
        'pesky.defaults',
        ],
    # distuils commands
    entry_points = {
        "distutils.commands": [
            "set_default = pesky.defaults.distcmd:set_default",
            ],
        },
    # test configuration
    test_suite="test",
    tests_require=["nose >= 1.3.1"]
)

# -*- coding: utf-8 -*-

import sys

from setuptools import find_packages
from setuptools import setup

import fastentrypoints

if not sys.version_info[0] == 3:
    sys.exit("Python 3 is required. Use: 'python3 setup.py install'")

dependencies = [
    "icecream",
    "click",
    "click-auto-help @ git+https://git@github.com/jakeogh/click-auto-help",
    "mptool @ git+https://git@github.com/jakeogh/mptool",
]

config = {
    "version": "0.1",
    "name": "bnftool",
    "url": "https://github.com/jakeogh/bnftool",
    "license": "ISC",
    "author": "Justin Keogh",
    "author_email": "github.com@v6y.net",
    "description": "functions related to Backus-Naur Form (BNF) notation",
    "long_description": __doc__,
    "packages": find_packages(exclude=["tests"]),
    "package_data": {"bnftool": ["py.typed"]},
    "include_package_data": True,
    "zip_safe": False,
    "platforms": "any",
    "install_requires": dependencies,
    "entry_points": {
        "console_scripts": [
            "bnftool=bnftool.bnftool:cli",
        ],
    },
}

setup(**config)

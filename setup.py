#!/usr/bin/env python
from setuptools import setup

setup(
    name = "ricerous",
    version = "0.0.1",
    description = ("Portable wiki for ricing"),
    packages = ["ricerous"],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX"
    ],
    package_data = {
        "ricerous":[
            "rice.kv",
            "plugins/*.py",
            "json/*.json"
        ]
    },
    scripts = [
        "scripts/ricerous"
    ],
    install_requires = [
        "kivy",
        "pygame",
        "cython"
    ]
)

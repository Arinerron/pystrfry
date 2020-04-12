#!/usr/bin/env python3

from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name = 'pystrfry',
    version = '1.0.2',
    license = 'BSD-3-Clause',
    description = 'a tool for solving those annoying strfry CTF challenges',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'Aaron Esau',
    author_email = 'redpwn@aaronesau.com',
    packages = ['strfry'],
    scripts = ['scripts/strfry'],
    python_requires = '>=3.6'
)

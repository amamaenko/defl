#!/usr/bin/python
# -*- coding: utf8 -*-
"""Setup script for defl"""

from setuptools import setup

setup(name='defl',
      version="0.1.0",
      description='CLI tool that scans local file directories for duplicates',
      author="Anton Mamaenko",
      author_email='amamaenko at gmail.com',
      packages=['defl'],
      install_requires=['tqdm'])

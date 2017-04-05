#!/usr/bin/python
# -*- coding: utf8 -*-
"""Core functions for the Defl package
"""
from typing import List

import defl.fileutil as fileutil


def find_duplicates(dirs: List) -> List:
    """Performs the search for duplicates in given folders
    """
    '''found_files = []
    found_files.append("Hello")
    return found_files
    '''

    return fileutil.scan_directory(dirs[0])

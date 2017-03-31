#!/usr/bin/python
# -*- coding: utf8 -*-
"""Core functions for the Defl package
"""
import os
import itertools
from typing import List, Dict

def find_duplicates(dirs: List) -> List:
    """Performs the search for duplicates in given folders
    """
    '''found_files = []
    found_files.append("Hello")
    return found_files
    '''

    return scan_directory(dirs[0])

def scan_directory(dir_path: str) -> Dict:
    """Scans directory for files and returns the dictionary of file info
    descriptors with file paths as keys.
    """
    dir_walk_items = os.walk(dir_path)

    # TODO: slice first 5 items for testing
    dir_walk_items = itertools.islice(dir_walk_items, 5)

    for dir_walk_item in dir_walk_items:
        print()
        print(dir_walk_item)

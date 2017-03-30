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
    for i in dirs:
        print(i)

    return scan_directory(dirs[0])

def scan_directory(dir_path: str) -> Dict:
    """Scans directory for files and returns the dictionary of file info
    descriptors with file paths as keys.
    """
    results = os.walk(dir_path)
    my = itertools.islice(results, 5)
    for i in my:
        print(i)

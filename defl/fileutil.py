#!/usr/bin/python
# -*- coding: utf8 -*-
"""Module defines filtering operations on scanned files, including the
list of allowed files to scan.
"""
import os
import itertools
from typing import Dict

from defl.fileinfo import FileInfo

ALLOWED_FILES = []


def scan_directory(dir_path: str) -> Dict:
    """Scans directory for files and returns the dictionary of file info
    descriptors with file paths as keys.
    """
    dir_walk_items = os.walk(dir_path)

    # TODO: slice first 5 items for testing
    dir_walk_items = itertools.islice(dir_walk_items, 5)

    files_tree = []
    for dir_walk_item in dir_walk_items:
        path_to_dir = dir_walk_item[0]
        file_names = dir_walk_item[2]
        for file_name in file_names:
            files_tree.append(os.path.join(path_to_dir, file_name))

        for i in files_tree:
            print("{0}".format(i))


def collect_file_info(file_paths: str) -> Dict[FileInfo]:
    file_infos = {}
    return
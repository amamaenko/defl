#!/usr/bin/python
# -*- coding: utf8 -*-
"""Module defines filtering operations on scanned files, including the
list of allowed files to scan.
"""
import os
from typing import List

from defl.fileinfo import FileInfo

# List of files to ignore, such as system cache files, etc.
IGNORED_FILES = set(['Thumbs.db'])
ALLOWED_FILES = []


def get_files_in_dir(dir_path: str) -> List[FileInfo]:
    """Scans directory for files and returns the list of FileInfo items.
    """
    dir_walk_items = os.walk(dir_path)

    all_files = []
    for dir_walk_item in dir_walk_items:
        path_to_dir = dir_walk_item[0]
        file_names = dir_walk_item[2]
        for file_name in file_names:
            if file_name not in IGNORED_FILES:
                all_files.append(
                    FileInfo.create(path_to_dir, file_name)
                )

    return all_files

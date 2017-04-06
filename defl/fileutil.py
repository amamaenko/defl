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
                    _create_file_info(path_to_dir, file_name)
                )

    return all_files

def _create_file_info(file_path: str, file_name: str)->FileInfo:
    """Collects the information about the physical file on disk, and factories

    a FileInfo object. Note that the function takes path to the file's location
    and the file's name as two separate arguments.

    Args:
        file_path(str): path to the location of the file on the physical disk
        file_name(str): name of the file
    """

    full_path = os.path.join(file_path, file_name)
    info = os.stat(full_path)

    new_file_info = FileInfo(
        path=file_path,
        name=file_name,
        size=info.st_size)
    return new_file_info

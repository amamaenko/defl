#!/usr/bin/python
# -*- coding: utf8 -*-
"""Contains utility methods used by the cli module
"""
from typing import List, Tuple
from defl.fileinfo import FileInfo

FileInfoPair = Tuple[FileInfo, FileInfo]
FileInfoPairs = List[FileInfoPair]


def print_duplicates(pairs: FileInfoPairs):
    """Prints FileInfo pairs that are duplicate suspects

    Args:
        pairs(List): the list of tuples containing duplicate suspects' FileInfo
            descriptors
    """
    for pair in pairs:
        print("\"{0}\" \"{1}\"".format(pair[0].fpath, pair[1].fpath))

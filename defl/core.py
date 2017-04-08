#!/usr/bin/python
# -*- coding: utf8 -*-
"""Core functions for the Defl package
"""
from typing import List, Tuple
import itertools
from tqdm import tqdm

import defl.fileutil as fileutil
from defl.fileinfo import FileInfo


FileInfoPair = Tuple[FileInfo, FileInfo]


def find_duplicates(dirs: List[str]) -> List[FileInfo]:
    """The core function that serves as a root of all duplication finding
    operations.

    Args:
        dirs(List[str]): the list of directory paths
    """
    all_files = []
    for dir_name in dirs:
        all_files = all_files + fileutil.get_files_in_dir(dir_name)


    all_duplicate_suspects = _find_duplicates_suspects(all_files)

    return all_duplicate_suspects

def _find_duplicates_suspects(
        file_infos: List[FileInfo])->List[FileInfoPair]:
    """This method scans the list to find duplicate suspects as pairs, and
    returns them in a list.
    """
    duplicate_suspects = []
    # using a pseudo-UI `tqdm` library to track progress
    # total number of combinations is ~ n^2/2
    combinations_count = len(file_infos)*len(file_infos)/2
    with tqdm(total=combinations_count, unit='pairs', unit_scale=True) as pbar:
        for pair in itertools.combinations(file_infos, 2):
            if FileInfo.cmp_sz(pair[0], pair[1]):
                duplicate_suspects.append(pair)
            pbar.update()

    return duplicate_suspects

#!/usr/bin/python
# -*- coding: utf8 -*-
"""Core functions for the Defl package
"""
from typing import List, Tuple
import itertools
from tqdm import tqdm

import defl.fileutil as fileutil
from defl.fileinfo import FileInfo


def find_duplicates(dirs: List[str]) -> List[FileInfo]:
    """The core function that serves as a root of all duplication finding
    operations.

    Args:
        dirs(List[str]): the list of directory paths
    """
    all_files = []
    for dir_name in dirs:
        all_files = all_files + fileutil.get_files_in_dir(dir_name)


    all_duplicate_suspects = _find_duplicates_in_file_infos(all_files)

    for i in all_duplicate_suspects:
        print("{0} =?= {1}".format(str(i[0]), str(i[1])))

    return all_files

def _find_duplicates_in_file_infos(
        file_infos: List[FileInfo])->List[Tuple[FileInfo, FileInfo]]:
    """This method scans the list to find duplicate suspects as pairs, and
    returns them in a list
    """
    duplicate_suspects = []
    # using a pseudo-UI `tqdm` library to track progress
    # total number of combinations is n/2 using the math formula
    combinations_count = len(file_infos)*len(file_infos)/2
    with tqdm(total=combinations_count, unit='pairs', unit_scale=True) as pbar:
        for pair in itertools.combinations(file_infos, 2):
            if pair[0] == pair[1]:
                duplicate_suspects.append(pair)
            pbar.update()

    return duplicate_suspects

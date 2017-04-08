#!/usr/bin/python
# -*- coding: utf8 -*-
"""Core functions for the Defl package
"""
from typing import List, Tuple
import itertools
import hashlib
from tqdm import tqdm

import defl.fileutil as fileutil
from defl.fileinfo import FileInfo


FileInfos = List[FileInfo]
FileInfoPair = Tuple[FileInfo, FileInfo]
FileInfoPairs = List[FileInfoPair]


def find_duplicates(dirs: List[str]) -> List[FileInfo]:
    """The core function that serves as a root of all duplication finding
    operations.

    Args:
        dirs(List[str]): the list of directory paths
    """
    print()
    print("Scanning directories: {0}".format(str(dirs)))
    all_files = []
    for dir_name in dirs:
        all_files = all_files + fileutil.get_files_in_dir(dir_name)

    print("Total files found: {0}".format(len(all_files)))
    print()

    print("--------------------------------------------")
    print("| Searching duplicate suspects by file size|")
    print("--------------------------------------------")
    all_duplicate_suspects = _find_duplicates_suspects(all_files)
    print()
    print("--------------------------------------------")
    print("| Filtering duplicate suspects by md5 hash |")
    print("--------------------------------------------")
    filtered_duplicate_suspects = _filter_by_md5(all_duplicate_suspects)

    return filtered_duplicate_suspects

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

def _filter_by_md5(file_info_pairs: FileInfoPairs)->FileInfoPairs:
    count = len(file_info_pairs)
    filtered = None
    with tqdm(total=count, unit='pairs', unit_scale=True) as pbar:
        def _progress_comp_md5(pair: FileInfoPair)->bool:
            """Wrapper function to show progress during filtering"""
            pbar.update()
            return _comp_md5(pair)
        filtered = filter(_progress_comp_md5, file_info_pairs)
    result = list(filtered)
    return result

def _comp_md5(pair: FileInfoPair)->bool:
    """Calculates and compares the MD5 sums for two files given their FileInfo
    descriptors"""
    md5_1 = _calc_md5(pair[0])
    md5_2 = _calc_md5(pair[1])
    return md5_1 == md5_2

def _calc_md5(file_info: FileInfo)->str:
    """Computes an MD5 hash of  a file"""
    hash_md5 = hashlib.md5()
    for block in _read_blocks(file_info):
        hash_md5.update(block)
    return hash_md5.hexdigest()

def _read_blocks(file_info: FileInfo, blocksize: int=65536):
    """Reads a file from disk by small blocks to increase memory efficiency"""
    with open(file_info.fpath, 'rb') as afile:
        block = afile.read(blocksize)
        while len(block) > 0:
            yield block
            block = afile.read(blocksize)

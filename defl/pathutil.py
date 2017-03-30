#!/usr/bin/python
# -*- coding: utf8 -*-
"""This module provides utility functions to deal with file names provided
through the CLI interface: clean them of quotes, split into individual files,
strip from extra spaces, etc.

Note: this utility is using a naive approach, only relying on split and replace,
rather than on smart regular expressions or something like that.
"""
from typing import List
import os


class NotDirException(Exception):
    """Thrown by the pathutil module in case where a path that must be a dir
    already exists, and is a file.
    """
    pass

class NotFoundException(Exception):
    """Thrown by the pathutil module in case where the path cannot be found.
    """
    pass


def str_to_tokens(user_str: str) -> List[str]:
    """Split the given string into elements using the rules of separation.
    In our case the rule is simple, each token is separated by a comma (,)
    character.
    "Hello World, Yes, sir!" - will be transofrmed into:
    ["Hello World", "Yes", "sir!"]
    """
    return user_str.split(',')


def token_to_dirname(token: str) -> str:
    """Cleans up a given token from quotes, strip from spaces, etc.

    The returned string is a valid directory name on the current platform.

    Args:
        token(str): 'dirty' folder name obained from the user through CLI
    Returns:
        valid directory name
    """
    foldername = token
    foldername = foldername.replace('"', '')
    foldername = foldername.strip(' ')
    return foldername


def str_to_dirnames(user_str: str) -> List[str]:
    """Transform the string that 'supposedly' contains the list of folders to
    search into a list of valide directory names.

    Args:
        user_str(str): string obtained from the CLI interface
    Return:
        list of directory names
    """
    tokens = str_to_tokens(user_str)
    foldernames = []
    for token in tokens:
        foldernames.append(token_to_dirname(token))

    return foldernames

def get_abs_dir_path(dir_name: str) -> str:
    """Returns the full path to the directory on the local machine.

    This methods checks if the directory already exists, if not - raise the
    `NotFoundExcpetion`.
    Then the method checks if the specified name is a file, if not - raise the
    `NotDirException`.

    Args:
        dir_name(str): name of the directory relative to the invocation of the
        util.

    Returns:
        Absolute path on the local filesystem.
    """
    dir_name = os.path.expanduser(dir_name)
    abs_path = dir_name if os.path.isabs(dir_name) \
        else os.path.abspath(dir_name)

    if not os.path.exists(abs_path):
        raise NotFoundException("Dir {0} cannot be found".format(abs_path))

    if os.path.isdir(abs_path):
        return abs_path
    else:
        raise NotDirException(
            "The name {0} already exists and is not a dir".format(abs_path))


def str_to_abs_paths(user_str: str)->List[str]:
    """Transforms the string input by user into the list of absolute directory
    paths on the local file system. These paths are guaranteed to exist and be
    directories, not files.

    Args:
        user_str(str): string that contains the list of dir names provided by
            the user through CLI interface.

    Returns:
        List[str]: list of absolute paths on the local file system
    """
    local_dir_paths = str_to_dirnames(user_str)
    abs_dir_paths = map(get_abs_dir_path, local_dir_paths)

    return abs_dir_paths

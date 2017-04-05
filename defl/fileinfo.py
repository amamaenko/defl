#!/usr/bin/python
# -*- coding: utf8 -*-
"""Contains the class definition for the file information used in searching for
duplicates"""


class FileInfo(object):
    """Encapsulates information about a file. It is used in searching for
    duplicates.

    Parameters:
        path(str): full path to the file on a local file system
        name(str): name of the file
        size(int): size of the file in bytes
    """
    def __init__(self, path: str, name: str, size: int):
        self.path = path
        self.name = name
        self.size = size

    def __eq__(self, other):
        return (self.name == other.name) and (self.size == other.size)

    def __hash__(self):
        return hash((self.name, self.size))

    def __repr__(self):
        return " path: {0}\n name: {1}\n size: {2}\n".format(
            self.path, self.name, self.size
        )

    def __str__(self):
        return self.__repr__()

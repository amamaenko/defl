#!/usr/bin/python
# -*- coding: utf8 -*-
"""Contains the class definition, and instance methods for the file information
used in searching for duplicates
"""
import os


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
        return "path: {0}\nname: {1}\nsize: {2}".format(
            self.path, self.name, self.size
        )

    def __str__(self):
        return self.__repr__()

    @property
    def fpath(self):
        """Returns the full path to the file object
        """
        return os.path.join(self.path, self.name)

    @classmethod
    def cmp_sz(cls, first, second):
        """Compare sizes of two FileInfo objects
        """
        return first.size == second.size

    @classmethod
    def cmp(cls, first, second):
        """Compares to FileInfo objects using a more complex algorithm than
        simply checking the name and the size
        """
        return first == second

    @classmethod
    def create(cls, file_path: str, file_name: str):
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

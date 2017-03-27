#!/usr/bin/python
# -*- coding: utf8 -*-
"""This module provides the entry point for CLI-based user interface to the
defl application
"""
import argparse
import defl.pathutil
import defl.core

HLP_DESC = """
Finds the duplicated image files 
"""


def run():
    """Main entry point for parsing cli-arguments and launching the core
    function of the app.
    """
    myparser = argparse.ArgumentParser(description=HLP_DESC)
    myparser.add_argument(
        "-f", "--folders", action="store",
        default="",
        required=True,
        help="Specify the list of folders whose content must be scanned",
        dest="src_folders")
    myparser.add_argument(
        "--dry-run", action='store_true',
        default=False,
        help="Prepare the command but not execute it. Print parsed arguments.",
        dest="is_dry")
    flags = myparser.parse_args()

    folder_names = defl.pathutil.str_to_foldernames(flags.src_folders)
    if flags.is_dry:
        print(flags)
        print(folder_names)
    else:
        defl.core.find_duplicates(folder_names)

    return 0

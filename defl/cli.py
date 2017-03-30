#!/usr/bin/python
# -*- coding: utf8 -*-
"""This module provides the entry point for CLI-based user interface to the
defl application
"""
import argparse
import defl.pathutil
import defl.core

APP_HELP_STR = """
Finds the duplicated image files 
"""
SOURCE_CMD_HELP_STR = """
Specify the list of source directories that will be scanned for duplicates
"""

DRY_RUN_CMD_HELP_STR = """
Prepare the command but not execute it. Print parsed arguments.
"""


def run():
    """Main entry point for parsing cli-arguments and launching the core
    function of the app.
    """
    myparser = argparse.ArgumentParser(description=APP_HELP_STR)
    myparser.add_argument(
        "-s", "--source", action="store",
        default="",
        required=True,
        help=SOURCE_CMD_HELP_STR,
        dest="src_folders")
    myparser.add_argument(
        "--dry-run", action='store_true',
        default=False,
        help=DRY_RUN_CMD_HELP_STR,
        dest="is_dry")
    flags = myparser.parse_args()

    folder_names = list(defl.pathutil.str_to_abs_paths(flags.src_folders))
    if flags.is_dry:
        print(flags)
        print(folder_names)
    else:
        defl.core.find_duplicates(folder_names)

    return 0

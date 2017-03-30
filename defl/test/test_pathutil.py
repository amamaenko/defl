#!/usr/bin/python
# -*- coding: utf8 -*-
"""Checks the path manipulation utiltities
"""
import os
import os.path
import shutil
import pytest
import defl.pathutil as pathutil


LOCAL_TEMP_DIR_NAME = 'temp'


@pytest.fixture(scope="module")
def temp_dir():
    """Fixture provides the temporary directory relative to the local path"""
    temp_path = os.path.abspath(LOCAL_TEMP_DIR_NAME)
    if os.path.exists(temp_path):
        shutil.rmtree(temp_path)

    os.mkdir(temp_path)
    yield temp_path  # provide the fixture value
    shutil.rmtree(temp_path) # tear down the temporary directory


def test_str_to_tokens():
    """checks simple toeknization of the input string
    """
    test_input = '"Hello World, Yes, sir!"'
    ref_output = ['"Hello World', ' Yes', ' sir!"']
    tested_output = pathutil.str_to_tokens(test_input)

    assert tested_output == ref_output

def test_token_to_dirname():
    """Checks cleaning the token from 'junk' characters so that it's a valid
    directory name.
    """
    test_input1 = '" Hi"'
    ref_output1 = 'Hi'
    tested_output1 = pathutil.token_to_dirname(test_input1)

    assert tested_output1 == ref_output1

def test_str_to_dirnames():
    """Checks that an input string gets transformed into a list of valid
    directory names.

    For this suite it's also a sort of integration test for the pathutil
    operations on directory names parsing.
    """
    test_input = '"Hello World, Yes, sir!"'
    ref_output = ['Hello World', 'Yes', 'sir!']
    tested_output = pathutil.str_to_dirnames(test_input)
    assert ref_output == tested_output


def test_get_abs_dir_path(temp_dir):
    """Checks the operation on retreiving absolute file path

    Args:
        temp_dir: fixture for the temporary test directory
    """
    sub_dir = os.path.join(temp_dir, 'sub')
    os.mkdir(sub_dir)

    test_input1 = temp_dir
    ref_output1 = os.path.abspath(test_input1)
    tested_output1 = pathutil.get_abs_dir_path(test_input1)
    assert ref_output1 == tested_output1

    test_input2 = sub_dir
    ref_output2 = os.path.abspath(sub_dir)
    tested_output2 = pathutil.get_abs_dir_path(test_input2)
    assert ref_output2 == tested_output2

def test_str_to_abs_paths_normal(temp_dir):
    """Checks the main user flow for the pathutil.str_to_abs_paths method

    Args:
        temp_dir: fixture for the temporary test directory
    """
    sub_dir = os.path.join(temp_dir, 'sub1')
    os.mkdir(sub_dir)

    test_input1 = "{0}, {1}".format(temp_dir, sub_dir)
    ref_output1 = [
        os.path.abspath(temp_dir),
        os.path.abspath(sub_dir)
    ]
    tested_output1 = pathutil.str_to_abs_paths(test_input1)
    assert ref_output1 == tested_output1

def test_str_to_abs_paths_errors(temp_dir):
    """Check how the pathutil.str_to_abs_paths handles various error situations
    """
    # we create a directory that should not contain anything
    empty_sub_dir = os.path.join(temp_dir, 'empty')
    os.mkdir(empty_sub_dir)

    # first check that the SUT fails if it's given a non-existing dir
    # there is no assert necessary in this part
    non_existing_path = os.path.join(empty_sub_dir, "Idontexist")
    test_input1 = "{0}".format(non_existing_path)
    with pytest.raises(pathutil.NotFoundException):
        pathutil.str_to_abs_paths(test_input1)

    file_path = os.path.join(temp_dir, 'a.txt')
    with open(file_path, 'w+'):
        pass

    test_input2 = "{0}".format(file_path)
    with pytest.raises(pathutil.NotDirException):
        pathutil.str_to_abs_paths(test_input2)

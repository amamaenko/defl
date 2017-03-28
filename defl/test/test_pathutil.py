#!/usr/bin/python
# -*- coding: utf8 -*-
"""Checks the path manipulation utiltities
"""
import os
import pytest
import defl.pathutil as pathutil


TEMP_DIR_NAME = 'temp'


@pytest.fixture(scope="module")
def temp_dir():
    """Fixture provides the temporary directory relative to the local path"""
    temp_dir = os.mkdir(TEMP_DIR_NAME)
    yield temp_dir  # provide the fixture value
    os.rmdir(TEMP_DIR_NAME) # tear down the temporary directory
    

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

def test_get_abs_dir_path(tmpdir):
    """Checks the operation on retreiving absolute file path
    """
    tmpdir.mkdir('a')
    tmpdir.

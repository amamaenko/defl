# -*- coding: utf8 -*-
"""Checks for the hashing and file checksum calculations
"""
import defl.core

TEST_DIR = "defl/test/samples"


def test_duplicates():
    """Check that duplicates found correctly amongst sample data"""
    duplicates = defl.core.find_duplicates([TEST_DIR])
    assert len(duplicates) > 0

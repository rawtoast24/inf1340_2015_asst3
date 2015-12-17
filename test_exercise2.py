#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import pytest
import os
from exercise2 import decide

DIR = "test_jsons/"
os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Reject", "Quarantine","Reject", "Reject", "Reject"]

def test_visitors():
    """
    Travellers that are visiting KAN. All their documents have to be filled and have appropriate entries
    """
    assert decide("test_visitor.json", "countries.json") ==\
        ["Accept", "Reject", "Quarantine", "Accept", "Reject", "Accept"]
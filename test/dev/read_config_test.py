import pytest

from ...src import read_config

def test_file_reading():
    configuration = read_config.Config("../config.cfg")

    configuration.get_config("field")
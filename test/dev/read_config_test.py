from pathlib import Path
import pytest

from ...src import read_config


def test_get_config():
    configuration = read_config.Config(path="config.cfg")

    # A valid field returns the actual value
    assert configuration.get_config(["version"])['version'] == "0.1.1"

    # Fields with characters that are subset of valid fields
    with pytest.raises(ValueError):    
        configuration.get_config("vers")
    
    # Fields that do not exist
    with pytest.raises(ValueError):
        configuration.get_config("Non existant field")
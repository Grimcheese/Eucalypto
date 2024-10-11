"""
Unit testing for db module

"""


import pytest

from ...src import db, read_config

@pytest.fixture



def test_get_credentials():
    # Move config to fixture
    config = read_config.Config()

    # Check that no errors are raised while getting credentials from Vault
    
    # Raises KeyError when attempting vault connection in dev test
    with pytest.raises(KeyError):
        db.get_db_credentials(config, "vault")

    db.get_db_credentials(config, "local")    
    
    
    
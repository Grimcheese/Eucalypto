"""
Unit testing for db module

"""


import pytest

from ...src import db, read_config
from pathlib import Path

@pytest.fixture
def test_config_path():
    return(Path("test_config.cfg"))


@pytest.fixture
def create_config(test_config_path):
    """Create a config file to be used for testing"""

    # Write lines to config file
    with open(test_config_path, 'w') as f:
        f.write("db_auth = local\n")
        f.write("db_name = test_db_name\n")
        f.write("db_username = test_db_username\n")
        f.write("db_password = test_db_password\n")
        f.write("db_url = localhost\n")
        f.write("db_port = 12345\n")
    
    # Yield fixture
    yield

    # Delete config file
    test_config_path.unlink()


def test_get_credentials(test_config_path, create_config):
    """Unit test for get_db_credentials.
    
    In development testing only the local authentication method
    is available, so vault authentication testing should fail.
    """

    config = read_config.Config(path=test_config_path)
    
    # Raises KeyError when attempting vault connection in dev test
    with pytest.raises(Exception):
        db.get_db_credentials(config, "vault")

    # Test local configuration file authentication
    db_credentials = db.get_db_credentials(config, "local")    
    assert db_credentials['db_name'] == "test_db_name"
    assert db_credentials['db_username'] == 'test_db_username'
    assert db_credentials['db_password'] == 'test_db_password'
    assert db_credentials['db_url'] == 'localhost'
    assert db_credentials['db_port'] == '12345'
    
    
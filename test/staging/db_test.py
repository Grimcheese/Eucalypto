import pytest

from ... import db

def test_db_init():
    # Assert that with no environment variables, KeyError is raised
    with pytest.raises(KeyError):
        test_db = db.db_connect()
    
    
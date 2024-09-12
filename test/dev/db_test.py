import pytest

from ...src import db

def test_get_credentials():
    # Check that no errors are raised while getting credentials from Vault
    
    # Raises KeyError when attempting vault connection in dev test
    with pytest.raises(KeyError):
        db.get_db_credentials("vault")

    db.get_db_credentials("local")    
    
    
    
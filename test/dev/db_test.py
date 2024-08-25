import pytest

from ... import db

def test_get_credentials():
    # Check that no errors are raised while getting credentials from Vault
    db.get_db_credentials()
    
    
    
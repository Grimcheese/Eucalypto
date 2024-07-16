"""The database API for Eucalypto"""

import psycopg2
import hvac

def get_db_credentials(self):
    """Use Vault credential storage for db credentials"""

    client = hvac.Client(url="http://vault.grimnet.work:8200")
    return client


def create_connection(self):
    pass

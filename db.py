"""The database API for Eucalypto"""

import psycopg2
import hvac
import os
import json

def load_configuration():
    """Load the configuration file"""
    with open(".secrets/.config.json", 'r') as config_file:
        conf_data = json.load(config_file)
    print(conf_data.keys())
    return conf_data

def get_db_credentials(conf_data):
    """Use Vault credential storage for db credentials"""


    # Initialise vault client using TLS
    client = hvac.Client(
        url="https://vault.grimnet.work:8200",
        verify=True
    )

    # Get secret-id
    resp = client.auth.approle.generate_secret_id(
        role_name='eucalypto',
        wrap_ttl='1m'
    )

    print(resp)

    # Login using approle
    client.auth.approle.login(
        role_id=conf_data['role_id'],
        secret_id="b67c3c4c-3738-b15d-3f25-00d8ec0306a1"
    )
    
    print(client.is_authenticated())
    
    resp = client.auth.approle.read_role_id(
        role_name='some-role',
    )
    print(f'AppRole role ID for some-role: {resp["data"]["role_id"]}')

    secret_version_response = client.secrets.kv.v2.read_secret_version(
       path="eucalypto"
    )

    print(f"Secret response - {secret_version_response}")

    return client


def create_connection(self):
    pass


if __name__ == '__main__':
    #conf_data = load_configuration()
    #get_db_credentials(conf_data)
    print(os.environ['DB_NAME'])
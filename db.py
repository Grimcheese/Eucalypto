"""The database API for Eucalypto"""

import psycopg2
import hvac
import os
import json

def db_connect(dbname=None, user=None, password=None):
    """Create new database connection for session
    
    Args:
        dbname: Name of database to access
        user: Username to access the database with
        password: Password to access user account with
    
    Return: A psycopg2 connection object referncing the database
        that has been connected to. Return of None means there
        was an issue with connecting to the database.
    """
    
    if dbname == None or user == None or password == None:
        # Default to using environment values
        dbname=os.environ['EUCALYPTO_DB_NAME']
        user=os.environ['EUCALYPTO_DB_USER']
        password=os.environ['EUCALYPTO_DB_PASSWORD']

    try:    
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password
        )

        return connection
    except psycopg2.OperationalError as e:
        return None


def close(connection):
    """Close the connection to psycopg2 database"""
    connection.close()


def query(connection, query, params):
    """Create and send an SQL query with parameters to database"""
    cursor = connection.cursor()
    
    cursor.execute(query, params)
    results = cursor.fetchall()

    connection.commit()
    cursor.close()

    return results
    

"""Old db functions, may be redundant with Drone CI/CD system."""

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
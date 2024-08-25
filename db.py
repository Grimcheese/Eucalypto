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
        # Get credentials
        
        credentials = get_db_credentials()
        dbname = credentials["db_name"]
        user = credentials["db_username"]
        password = credetials["db_password"]
        

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

def get_db_credentials():
    """Use Vault credential storage for db credentials"""

    #app-role-id = os.environ["DEV-APPROLE-ID"]

    # Initialise vault client using TLS
    client = hvac.Client(
        url="https://vault.grimnet.work:8200",
        verify=True
    )

    # Login using approle
    client.auth.approle.login(
        role_id="55cb6ff6-8186-9c0c-52e7-9d7faa5ff4ab"
    )

    if client.is_authenticated():
        print("Vault authentication successful!")
    else:
        print("Unable to autheticate with Vault server")

    secret = client.secrets.kv.v2.read_secret_version(
        path="/eucalypto/db-info",
        mount_point="kv-v2",
        raise_on_deleted_version=True
    )

    
    db_info = {
        'db_name': secret['data']['data']['db_name'],
        'db_username': secret['data']['data']['db_username'],
        'db_password': secret['data']['data']['db_password']}
    

    ### Old method for getting creds from environment - could use in future versions
    #dbname=os.environ['EUCALYPTO_DB_NAME']
    #user=os.environ['EUCALYPTO_DB_USER']
    #password=os.environ['EUCALYPTO_DB_PASSWORD']

    return db_info



if __name__ == '__main__':
    #conf_data = load_configuration()
    get_db_credentials()
    #print(os.environ['DB_NAME'])
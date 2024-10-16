"""The database API for Eucalypto"""

import psycopg2
import hvac
import os
import json

import read_config

def db_connect(config, dbname=None, user=None, password=None):
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
        
        # Determine database authentication method using config file
        auth_method = config.db_auth()

        credentials = get_db_credentials(config, auth_method)
        db_url = credentials["db_url"]
        db_port = credentials["db_port"]
        dbname = credentials["db_name"]
        user = credentials["db_username"]
        password = credentials["db_password"]
        

    connection = psycopg2.connect(
        host=db_url,
        port=db_port,
        dbname=dbname,
        user=user,
        password=password
    )

    return connection
   


def close(connection):
    """Close the connection to psycopg2 database"""
    connection.close()


def query(connection, query, params=None):
    """Create and send an SQL query with (optional) parameters to database
    
    Arguments:
        connection: The database connected object being accessed.
        query: String with SQL query
        params: Any parameters that are to be added to the SQL query. 
            This argument is optional and has a default value of None.
    
    Returns: Any results from the query.
    """
    
    cursor = connection.cursor()
    
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    # Will raise ProgrammingError if no results
    # TODO catch the exception on no results
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


def get_db_credentials(config, auth_method):
    """Get database credentials from authentication method"""

    if auth_method == 'vault':
        return vault_authentication(config)
    elif auth_method == 'local':
        return config_file_authentication(config)
    else:
        # TODO Raise DatabaseAuthError
        raise Exception(f"Invalid authentication method: {auth_method}")

    ### Old method for getting creds from environment - could use in future versions
    #dbname=os.environ['EUCALYPTO_DB_NAME']
    #user=os.environ['EUCALYPTO_DB_USER']
    #password=os.environ['EUCALYPTO_DB_PASSWORD']


def config_file_authentication(config):
    """Authentication method using the configuration file."""

    # Retrieve db url, name, username and password from config file
    db_info = config.get_config("db_url", "db_port", "db_name", "db_username", "db_password")

    return {
        'db_url': db_info["db_url"],
        'db_port': db_info["db_port"],
        'db_name': db_info['db_name'],
        'db_username': db_info['db_username'],
        'db_password': db_info['db_password']}



def vault_authentication(config):
    """DB authentication method using Vault server."""
    
    vault_url = config.get_config("vault_server_url")

    app_role_id = os.environ["ROLE_ID"]

    # Initialise vault client using TLS
    client = hvac.Client(
        url=vault_url,
        verify=True
    )

    # Login using approle
    client.auth.approle.login(
        role_id=app_role_id
    )

    if client.is_authenticated():
        print("Vault authentication successful!")
    else:
        print("Unable to autheticate with Vault server")
        raise Exception("Unable to authenticate with Vault server")

    secret = client.secrets.kv.v2.read_secret_version(
        path="/eucalypto/db-info",
        mount_point="kv-v2",
        raise_on_deleted_version=True
    )

    return {
        'db_name': secret['data']['data']['db_name'],
        'db_username': secret['data']['data']['db_username'],
        'db_password': secret['data']['data']['db_password']}


if __name__ == '__main__':
    #conf_data = load_configuration()
    get_db_credentials()
    #print(os.environ['DB_NAME'])
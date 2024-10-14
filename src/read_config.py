"""
    Module to handle reading the eucalypto config file.
"""

from pathlib import Path

DEFAULT_PATH = Path("config.cfg")

class Config:
    def __init__(self, **setup_values):
        if 'path' in setup_values:
            self.fpath = Path(setup_values['path'])
            self.fpath.resolve()
        else:
            self.fpath = DEFAULT_PATH

        self._initialise_config()


    def _initialise_config(self):
        """Verify config file and store all fields"""

        # Verify config file syntax, etc...

        self.configuration = {}
        with open(self.fpath, 'r') as f:
            for line in f.readlines():
                # Skip empty lines and comments
                if line == '\n' or line[0] == '#':
                    continue

                print(line)
                if line[0] == '#':
                    continue
                line_parts = line.split("=")
                self.configuration[line_parts[0].strip()] = line_parts[1].strip()



    def get_config(self, fields):
        """Get a field from the config file.

        Raises a ValueError if searching for field that does not exist
        in config file.
        
        Params:
        @field: The fields in config file to read.
        
        @returns: The value stored in the config file under the specified field
        """
        
        results = {}
        for field in fields:
            if field in self.configuration.keys():
                print(f"Found {field}")
                results[field] = self.configuration[field]
            else:
                raise ValueError(f"Field: {field}, not set in configuration")
    
        return results
    

    def db_auth(self):
        """Determine db authentication method using config setup."""

        valid_config_values = ["vault", "local"]

        try:
            auth_method = self.get_config("auth")
            print(auth_method)
            if auth_method in valid_config_values:
                return auth_method
            else:
                #TODO raise customer InvalidConfig exception
                pass
        except ValueError as e:
            #TODO raise custom InvalidConfig exception
            pass


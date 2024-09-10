"""
    Module to handle reading the eucalypto config file.
"""

from pathlib import Path

class Config:
    def __init__(self, **setup_values):
        self.fpath = Path(setup_values['path'])


    def get_config(self, field):
        """Get a field from the config file.
        
        Params:
        @field: The field in config file to read
        
        @returns: The value stored in the config file under the specified field
        """

        with open(self.fpath, 'r') as f:
            for line in f.readline():
                print(line)


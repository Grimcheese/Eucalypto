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



    def get_config(self, field):
        """Get a field from the config file.

        Raises a ValueError if searching for field that does not exist
        in config file.
        
        Params:
        @field: The field in config file to read
        
        @returns: The value stored in the config file under the specified field
        """
        
        
        with open(self.fpath, 'r') as f:
            for line in f.readlines():
                print(line)
                if field in line: 
                
                    print(f"Found {field} line: {line}")
                    return line.split("=")[1].strip()
        raise ValueError()
    

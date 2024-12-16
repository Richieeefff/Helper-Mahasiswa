import os
import json

DATA_FILE = "../user_data.json"

class JadwalModel:
    def __init__(self, username):
        self.userdata = DATA_FILE
        self.username = username
    
    def load_user_data(self):
        """Load user data from JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {}  # Return an empty structure if the file doesn't exist.
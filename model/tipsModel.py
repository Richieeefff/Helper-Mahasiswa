import json
import os

DATA_FILE = 'tips_belajar.json'

def load_tips_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_tips_data(tips_data):
    with open(DATA_FILE, 'w') as file:
        json.dump(tips_data, file, indent=4)

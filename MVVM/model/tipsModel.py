import json
import os

DATA_FILE = 'tips_belajar.json'

class TipsModel:
    def __init__(self):
        self.data_file = DATA_FILE
        self.tips = []

    def load_tips_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
            
        return {}

    def save_tips_data(self, tips_data):
        with open(self.data_file, 'w') as file:
            json.dump(tips_data, file, indent=4)

    def tambah_tips(self):
        admin = input("Masukkan nama anda: ")
        tips = input("Masukkan Tips: ")
        
        tips_data = self.load_tips_data()

        # Loop through the dictionary to get the first value
        for key in tips_data:
            if tips_data[key] == tips:
                return False
        
        tips_data[admin] = tips
        self.save_tips_data(tips_data)
        return True
    
    def lihat_tips(self):
        return self.load_tips_data()
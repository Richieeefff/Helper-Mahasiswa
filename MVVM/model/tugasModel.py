import os
import json

DATA_FILE = "../user_data.json"

class TugasModel:
    def __init__(self, username):
        self.data_file = DATA_FILE
        self.username = username
    
    def load_user_data(self):
        """Load user data from JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {}  # Return an empty structure if the file doesn't exist.
    
    def save_user_data(self, data):
        try:
            with open(self.data_file, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def find_user(self):
        """Find the user by username and return a reference to the user object."""
        user_data = self.load_user_data()
        for i, user in enumerate(user_data["users"]):
            if user["username"] == self.username:
                return user_data["users"][i], user_data  # Return both user and full data
        return None, user_data

    # Function to display scheduled tasks nicely
    def get_tugas(self):
        """Retrieve all tasks for the current user."""
        user, _ = self.find_user()  # Unpack the tuple to get the user reference

        if not user:
            return {"error": f"User '{self.username}' not found."}

        tasks = user.get("scheduled_tasks", [])
        if not tasks:
            return {"message": f"User '{self.username}' tidak punya tugas pending."}
        
        return {"tasks": tasks}

    def add_tugas(self, date, matkul, judul, desc, diff, dl):
        """Add a new task to the user's scheduled tasks."""
        user, user_data = self.find_user()  # Get user reference and full data

        if user:
            # Append the new task to the user's scheduled tasks
            user["scheduled_tasks"].append({
                'tanggal': date,
                'mata_kuliah': matkul,
                'judul': judul,
                'deskripsi': desc,
                'tingkat_kesulitan': diff,
                'tenggat': dl,
                'status': 'Belum Selesai'
            })

            # Save the updated data back to the file
            self.save_user_data(user_data)
            return True
        else:
            return False

    def selesai_tugas(self, tugasID):
        user, user_data = self.find_user()

        if user:
            if 1 <= tugasID <= len(user["scheduled_tasks"]):
                remove = user["scheduled_tasks"].pop(tugasID - 1)
                self.save_user_data(user_data)
                return f"Tugas {remove['judul']} berhasil dihapus"
            else:
                return None
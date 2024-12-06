import os
import json

DATA_FILE = 'user_data.json'

class MenuModel:
    def __init__(self, username):
        self.data_file = DATA_FILE
        self.username = username

    def load_user_data(self):
        """Load user data from JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {"users": []}  # Return an empty structure if the file doesn't exist.

    def find_user(self):
        """Find the user by username."""
        user_data = self.load_user_data()
        for user in user_data["users"]:
            if user["username"] == self.username:
                return user
        return None

    def get_user_info(self):
        """Retrieve user information, including task and schedule counts."""
        if self.username == "admin":
            return {
                "username": self.username,
                "task_count": None,
                "schedule_count": None,
            }
        user = self.find_user()
        if user:
            task_count = len(user["scheduled_tasks"])
            schedule_count = len(user["university_schedule"])
            return {
                "username": self.username,
                "task_count": task_count,
                "schedule_count": schedule_count,
            }
        else:
            raise ValueError("User not found.")

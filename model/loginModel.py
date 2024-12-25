import utils.helper as helper

def load_users():
    return helper.load_user_data()

def save_users(user_data):
    helper.save_user_data(user_data)

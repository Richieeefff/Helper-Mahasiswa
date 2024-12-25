import utils.helper as helper

def calculate_level(username, scaling_factor=100):
    database = helper.load_user_data()
    for user in database["users"]:
        if user["username"] == username:
            exp = user["exp"]
            return int((exp / scaling_factor) ** 0.5)
    return 0  

def showProfile(username):
   
    while True:
        database = helper.load_user_data()
        
        user = next((u for u in database["users"] if u["username"] == username), None)

        if not user:
            print(f"User '{username}' not found.")
            return

        # Display user profile
        helper.clear()
        print("\n--- User Profile ---")
        print(f"Username: {username}")
        print(f"Kamu mempunyai {len(user['scheduled_tasks'])} tugas pending.")
        print(f"Level: {calculate_level(username)}")
        print("\nOptions:")
        print("1. Refresh Profile")
        print("2. Exit")

        
        choice = input("Pilih degan angka: ")
        if choice == '1':
            continue  
        elif choice == '2':
            return
        else:
            print("\n Invalid input! Silakan coba lagi.")

        


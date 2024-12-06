from view.menuView import MenuView
from view.loginView import LoginView

def main():
    while True:
        login = LoginView()
        username = login.menu()

        if username:
            menu_view = MenuView(username)
            menu_view.display_menu()

if __name__ == "__main__":
    main()

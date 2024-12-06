from model.loginModel import LoginModel

class LoginViewModel:
    def __init__(self):
        self.model = LoginModel()

    def register_user(self, username, password):
        return self.model.register_user(username, password)

    def auth_user(self, username, password):
        return self.model.auth_user(username, password)

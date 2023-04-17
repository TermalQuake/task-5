class User:
    def __init__(self, login, password_hash, salt, role):
        self.login = login
        self.password_hash = password_hash
        self.salt = salt
        self.role = role

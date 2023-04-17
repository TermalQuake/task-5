import json
import hashlib
import os

class User:
    def __init__(self, login, password, salt, role):
        self.login = login
        self.password = password
        self.salt = salt
        self.role = role

def register_user(login, password, role='buyer'):
    salt = os.urandom(32) # генерируем случайную соль
    password_hash = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()
    user = User(login, password_hash, salt.hex(), role)
    user.password_hash = password_hash  # добавляем поле password_hash
    with open('users.txt', 'a') as f:
        f.write(json.dumps(user.__dict__) + '\n')




def login_user(login, password):
    # Найти пользователя в файле
    with open('users.txt', 'r') as f:
        for line in f:
            user_dict = json.loads(line)
            if user_dict['login'] == login:
                # Хэшировать введенный пароль с применением сохраненной соли и сравнить с сохраненным хэшем
                salt = bytes.fromhex(user_dict['salt'])
                password_hash = hashlib.sha256(password.encode() + salt).hexdigest()
                if password_hash == user_dict['password']:
                    # Создать объект пользователя без хэширования поля role и вернуть его
                    return User(user_dict['login'], user_dict['password'], user_dict['salt'], user_dict['role'])
                else:
                    return None


def get_all_users():
    # Получить список всех пользователей из файла
    users = []
    with open('users.txt', 'r') as f:
        for line in f:
            user_dict = json.loads(line)
            users.append(User(user_dict['login'], user_dict['password'], user_dict['salt'], user_dict['role']))
    return users

def change_password(login, password):
    # Найти пользователя в файле
    with open('users.txt', 'r') as f:
        users = []
        for line in f:
            user_dict = json.loads(line)
            if user_dict['login'] == login:
                # Сгенерировать новую соль и хэш пароля
                salt = os.urandom(32)
                password_hash = hashlib.sha256(password.encode() + salt).hexdigest()
                # Обновить информацию о пользователе в файле
                user_dict['password'] = password_hash
                user_dict['salt'] = salt.hex()
            users.append(user_dict)

    # Обновить файл с пользователями
    with open('users.txt', 'w') as f:
        for user_dict in users:
            f.write(json.dumps(user_dict) + '\n')


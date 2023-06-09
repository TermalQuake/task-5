from user import User
from auth import register_user, login_user, get_all_users, change_password

def main():
    # Запросить у пользователя действие: регистрация или авторизация
    action = input("Введите 'r' для регистрации или 'l' для авторизации: ")

    # Если пользователь выбрал регистрацию
    if action == 'r':
        # Запросить у пользователя логин и пароль
        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        # Зарегистрировать пользователя
        register_user(login, password)
        print("Пользователь зарегистрирован")

    # Если пользователь выбрал авторизацию
    elif action == 'l':
        # Запросить у пользователя логин и пароль
        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        # Авторизовать пользователя
        user = login_user(login, password)
        if user:
            print("Пользователь авторизован")

            # В зависимости от роли пользователя вызвать соответствующую функцию
            if user.role == 'admin':
                # Вывести список всех пользователей и предоставить возможность изменять их пароли
                users = get_all_users()
                print("Список всех пользователей:")
                for u in users:
                    print(u.login, u.role)
                print('Введите логин пользователя, для которого нужно изменить пароль:')
                login = input()
                print('Введите новый пароль:')
                password = input()
                change_password(login, password)
                print('Пароль для пользователя {} успешно изменен'.format(login))

            elif user.role == 'seller':
                # Вывести сообщение о том, что функционал скоро будет доступен для данной роли
                print("Вы вошли в личный кабинет продавца. Скоро здесь появится функционал для данной роли пользователя")
            elif user.role == 'buyer':
                # Вывести сообщение о том, что функционал скоро будет доступен для данной роли
                print("Вы вошли в личный кабинет покупателя. Скоро здесь появится функционал для данной роли пользователя")
        else:
            print("Неверный логин или пароль")

if __name__ == '__main__':
    main()

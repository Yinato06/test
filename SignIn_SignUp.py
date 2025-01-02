class Database:
    """Класс базы данных пользователей"""

    def __init__(self):
        # Инициализируем словарь для хранения данных пользователей
        self.data = {}

    def add_user(self, username: str, password: str) -> None:
        # Добавляем нового пользователя в базу данных
        self.data[username] = password


class User:
    """Класс пользователя, содержит атрибуты: логин, пароль."""

    def __init__(self, username: str, password: str, password_confirm: str) -> None:
        self.username = username

        if password_confirm == password:
            self.password = password


def sign_in():
    """
    Функция для входа существующего пользователя.
    Сравнивает введенный логин и пароль с хранящимися в базе данных.
    """
    while True:
        login = input('Input login: ')

        if login in database.data:
            password = input('Input password: ')

            if password in database.data[login]:
                print(f'Welcome, {login}.\n')
                break

            else:
                print('Incorrect password.\n')

        else:
            print('Incorrect login.\n')


def sign_up():
    """
    Функция для регистрации нового пользователя.
    Проверяет пароль и добавляет пользователя в базу данных.
    """
    while True:
        username = input('Input login: ')

        if username in database.data:
            print('Login has been busy.\n')
            continue

        password, password_confirm = input('Input password: '), input('Confirm password: ')

        if password != password_confirm:
            print('Passwords differ.\n')
            continue

        if len(password) < 8:
            print('The password must be 8 characters long.\n')
            continue

        if not any(char.isupper() for char in password):
            print('The password must contain at least 1 capital letter.\n')
            continue

        # Добавляем пользователя в базу данных и выходим из цикла
        database.add_user(username, password)
        print(f'User {username} successfully registered.\n')
        break


if __name__ == "__main__":
    database = Database()

    while True:

        try:
            choice = int(input('Choose an action.\n1 - Sign In\n2 - Sign Up\n'))

        except ValueError:
            print('Choice number 1 or 2.\n')
            continue

        if choice == 1:
            sign_in()

        if choice == 2:
            sign_up()

        print(database.data)

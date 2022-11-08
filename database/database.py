import sqlite3


class DataBase:
    def __init__(self, file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    # Создание таблиц базы данных.
    def create_database(self) -> sqlite3.OperationalError:
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY 
                AUTOINCREMENT 
                NOT NULL 
                UNIQUE,
            login STRING UNIQUE NOT NULL,
            password STRING NOT NULL
            );""")

        except sqlite3.Error as error:
            return error

        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users_passwords (
            id INTEGER PRIMARY KEY 
                AUTOINCREMENT 
                NOT NULL 
                UNIQUE,
            service STRING NOT NULL,
            login STRING NOT NULL, 
            password STRING NOT NULL,
            login_id INTEGER NOT NULL,
            FOREIGN KEY (login_id) REFERENCES logins (id)
            );""")

        except sqlite3.Error as error:
            return error

        try:
            self.connection.close()
        except sqlite3.Error as error:
            return error

    # Добавление внутреннего аккаунта в таблицу users.
    def insert_login_to_users(self,
                              login: str,
                              password: str
                              ) -> sqlite3.OperationalError:
        try:
            data = self.cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?",
                                       (login, password)).fetchone()
            if not data:
                self.cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login, password))
                self.connection.commit()
        except sqlite3.Error as error:
            return error

    # Получение логина и пароля из таблицы users.
    def select_login_from_users(self,
                                login: str
                                ) -> tuple or None or sqlite3.OperationalError:
        try:
            data = self.cursor.execute("SELECT login, password FROM users WHERE login = ?",
                                       (login,)).fetchone()
            if data:
                return data
            return None
        except sqlite3.Error as error:
            return error

    # Добавление логина и пароля в таблицу
    def insert_password_to_users_password(self,
                                          service: str,
                                          login: str,
                                          password: str,
                                          login_by_id: str
                                          ) -> sqlite3.OperationalError:
        try:
            data = self.cursor.execute("SELECT * FROM users_passwords WHERE service = ? AND login = ? AND password = ? "
                                       "AND login_id = (SELECT id FROM users WHERE login = ?)", (service, login,
                                                                                                 password,
                                                                                                 login_by_id)).fetchone()
            if not data:
                self.cursor.execute("INSERT INTO users_passwords (service, login, password, login_id) VALUES (?, ?, ?, "
                                    "(SELECT id FROM users WHERE login = ?))", (service, login, password, login_by_id))
                self.connection.commit()
        except sqlite3.Error as error:
            return error

    # Получение всех данных из таблицы users_passwords для проверки их наличия.
    def select_all_for_check(self,
                             service: str,
                             login: str,
                             login_by_id: str
                             ) -> tuple or None or sqlite3.OperationalError:
        try:
            data = self.cursor.execute("SELECT * FROM users_passwords WHERE service = ? AND login = ? AND login_id = ("
                                       "SELECT id FROM users WHERE login = ?)", (service, login, login_by_id)).fetchone()
            if data:
                return data
            return None
        except sqlite3.Error as error:
            return error

    # Получение всех сервиса, логина и пароля из таблицы users_passwords для вывода их на главном окне.
    def select_all_passwords(self,
                             login: str
                             ) -> tuple or None or sqlite3.OperationalError:
        try:
            data = self.cursor.execute("SELECT service, login, password FROM users_passwords WHERE login_id = ("
                                       "SELECT id FROM users WHERE login = ?)",
                                       (login,)).fetchall()
            if data:
                return data
            return None
        except sqlite3.Error as error:
            return error

    # Удаление данных из таблицы users_passwords.
    def delete_password(self,
                        service: str,
                        login: str,
                        login_by_id: str
                        ) -> sqlite3.OperationalError:
        try:
            self.cursor.execute("DELETE FROM users_passwords WHERE service = ? AND login = ? AND login_id = (SELECT id "
                                "FROM users WHERE login = ?)", (service, login, login_by_id))
            self.connection.commit()
        except sqlite3.Error as error:
            return error

    # Обновление пароля в таблице users_passwords.
    def update_password(self,
                        service: str,
                        login: str,
                        password: str,
                        login_by_id: str
                        ) -> sqlite3.OperationalError:
        try:
            data = self.cursor.execute("SELECT * FROM users_passwords WHERE service = ? AND login = ? AND login_id = ("
                                       "SELECT id FROM users WHERE login = ?)", (service, login, login_by_id)).fetchone()
            if data:
                self.cursor.execute("UPDATE users_passwords SET password = ? WHERE service = ? AND login = ? AND login_id "
                                    "= (SELECT id FROM users WHERE login = ?)", (password, service, login, login_by_id))
                self.connection.commit()
        except sqlite3.Error as error:
            return error

    # Получение данных из таблицы users_passwords для проверки существования этой записи.
    def select_password_for_check_update(
            self,
            service: str,
            login: str,
            password: str,
            login_by_id: str
            ) -> tuple or None or sqlite3.OperationalError:
        try:
            data = self.cursor.execute("SELECT * FROM users_passwords WHERE service = ? AND login = ? AND password = ?AND "
                                       "login_id = (SELECT id FROM users WHERE login = ?)", (service, login, password,
                                                                                             login_by_id)).fetchone()
            if data:
                return data
            return False
        except sqlite3.Error as error:
            return error

    # Получение заголовков таблицы users_passowords.
    def select_headers(self) -> list or sqlite3.OperationalError:
        try:
            return self.cursor.execute('PRAGMA table_info(users_passwords)').fetchall()
        except sqlite3.Error as error:
            return error

    # Закрытие подключения базы.
    def close_database(self) -> sqlite3.OperationalError:
        try:
            self.connection.close()
        except sqlite3.Error as error:
            return error

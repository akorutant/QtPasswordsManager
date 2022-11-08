from PyQt5.QtWidgets import QDialog, QStatusBar, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore

from py_ui.register_Ui import Ui_Dialog
from database.database import DataBase
from constants import KEYS


# Класс стартового окна. Появляется при запуске программы.
class StartDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(StartDialog, self).__init__(parent)
        self.parent = parent
        self.statusBar = QStatusBar(self)
        self.statusBar.move(4, 5)
        self.statusBar.resize(440, 15)
        self.database = DataBase('./users.sqlite')
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        try:
            # Подключение функций для кнопок.
            self.loginButton.clicked.connect(self.login_in)
            self.registerButton.clicked.connect(self.register_in)
        except Exception as error:
            return error

    # Вход во внутренний аккаунт в программе.
    def login_in(self):
        try:
            login = self.login.text()
            password = self.password.text()
            if login != "" and password != "":
                data = self.database.select_login_from_users(login)

                # Проверка на существование аккаунта.
                if not data:
                    self.statusBar.showMessage('Аккаунта с таким логином и паролем ещё не существует')
                elif data and login == str(data[0]) and password == str(data[1]):

                    # Если данные были правильно введены, то стартовое окно закрывается.
                    self.close()
                    self.passwords_data = self.database.select_all_passwords(login)

                    # Проверка на наличие паролей в базе данных.
                    if self.passwords_data:
                        self.parent.central_widget.passwordsTable.setRowCount(len(self.passwords_data))
                        self.parent.central_widget.passwordsTable.setColumnCount(len(self.passwords_data[0]))
                        for i, key in enumerate(self.passwords_data):
                            for j, item in enumerate(key):
                                new_item = QTableWidgetItem(str(item))
                                new_item.setFlags(QtCore.Qt.ItemIsEnabled)
                                self.parent.central_widget.passwordsTable.setItem(i, j, new_item)

                        # Установка названий столбцов, а также столбцы расстягиваются по ширине QTableWidget.
                        self.parent.central_widget.passwordsTable.setHorizontalHeaderLabels(KEYS)
                        header = self.parent.central_widget.passwordsTable.horizontalHeader()
                        header.setSectionResizeMode(0, QHeaderView.Stretch)
                        header.setSectionResizeMode(1, QHeaderView.Stretch)
                        header.setSectionResizeMode(2, QHeaderView.Stretch)

                    # После вывода данных открывается основной интерфейс программы.
                    self.parent.show()

                # Проверка на правильность пароля.
                elif login == data[0] and password != data[1]:
                    self.statusBar.showMessage('Вы неверно ввели пароль')

            # Проверка на случай, если поля ввода пустые.
            if login == "" and password == "":
                self.statusBar.showMessage('Вы не ввели логин и пароль')
            elif login == "":
                self.statusBar.showMessage('Вы не ввели логин')
            elif password == "":
                self.statusBar.showMessage('Вы не ввели пароль')
        except Exception as error:
            return error

    # Регистрация внутреннего аккаунта в программе
    def register_in(self):
        try:
            login = self.login.text()
            password = self.password.text()
            if login != "" and password != "":
                data = self.database.select_login_from_users(login)

                # Проверка на существование аккаунта
                if data:
                    self.statusBar.showMessage('Аккаунт с таким логином уже существует')
                else:
                    # Если аккаунта не существует, то он регистриуется, закрывается диалогове окно
                    # И открывается главное.
                    self.database.insert_login_to_users(login, password)
                    self.close()
                    self.parent.show()

            # Проверка на случай, если поля ввода пустые.
            if login == "" and password == "":
                self.statusBar.showMessage('Вы не ввели логин и пароль')
            elif login == "":
                self.statusBar.showMessage('Вы не ввели логин')
            elif password == "":
                self.statusBar.showMessage('Вы не ввели пароль')
        except Exception as error:
            return error
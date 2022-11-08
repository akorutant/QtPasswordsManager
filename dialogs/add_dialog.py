from PyQt5.QtWidgets import QDialog, QStatusBar, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore

from py_ui.add_logins_UI import Ui_QDialog
from database.database import DataBase
from functions.password_generator import PasswordGenerator
from constants import KEYS


# Класс диалогового окна для добавления данных в QTableWidget
class AddDialog(QDialog, Ui_QDialog):
    def __init__(self, parent=None):
        super(AddDialog, self).__init__(parent)
        self.parent = parent
        self.setModal(True)
        self.statusBar = QStatusBar(self)
        self.statusBar.move(4, 0)
        self.statusBar.resize(421, 15)
        self.setupUi(self)
        self.initUi()
        self.database = DataBase('./users.sqlite')

    def initUi(self):
        try:
            # Подключение функций для кнопок.
            self.generationPasswordCheckBox.clicked.connect(self.check_state)
            self.commitButton.clicked.connect(self.commit_data)
            self.generateButton.clicked.connect(self.generate_password)

            # Скрываются виджеты, которые должны появится только, если пользовтаель хочет сгенерировать пароль.
            self.specialSymbolsCheckBox.hide()
            self.numbersCheckBox.hide()
            self.lengthPasswordLabel.hide()
            self.lengthPasswordLine.hide()
            self.generateButton.hide()
        except Exception as error:
            return error

    # Функция для появляения диалогового окна.
    def show_add_logins_dialog(self):
        try:
            self.show()
        except Exception as error:
            return error

    # Проверка, хочет ли пользователь сгенерировать пароль.
    def check_state(self):
        try:
            # Если пользователь хочет сгенерировать пароль, то появлются нужные виджеты.
            # Поле ввода пароля блокируется для редактирования.
            if self.generationPasswordCheckBox.checkState():
                self.specialSymbolsCheckBox.show()
                self.numbersCheckBox.show()
                self.lengthPasswordLabel.show()
                self.lengthPasswordLine.show()
                self.generateButton.show()

                self.passwordLine.setReadOnly(True)
            # Если пользователь передумал генерировать пароль, то виджеты скрываются.
            # Поле ввода пароля разблокируется.
            else:
                self.specialSymbolsCheckBox.hide()
                self.numbersCheckBox.hide()
                self.lengthPasswordLabel.hide()
                self.lengthPasswordLine.hide()
                self.generateButton.hide()
                self.passwordLine.setReadOnly(False)
        except Exception as error:
            return error

    # Функция для подтверждения добавления данных и их вывод.
    def commit_data(self):
        try:
            service = self.serviceLine.text().lower()
            login = self.loginLine.text()
            password = self.passwordLine.text()
            self.login_by_id = self.parent.start_dialog.login.text()
            data = self.database.select_all_for_check(service, login, self.login_by_id)

            # Проверки на случай того, что поля будут пустые или логин и пароль уже добавлены.
            if data:
                self.statusBar.showMessage('Логин и пароль уже сохранены для этого сервиса')
            elif service == "":
                self.statusBar.showMessage('Вы не указали сервис')
            elif login == "":
                self.statusBar.showMessage("Вы не указали логин")
            elif password == "":
                self.statusBar.showMessage("Вы не указали пароль")
            else:
                # Добавление логина и пароля в базу данных и получение этих паролей.
                self.database.insert_password_to_users_password(service, login, password, self.login_by_id)
                self.passwords_data = self.database.select_all_passwords(self.login_by_id)
                if self.passwords_data:
                    # Вывод логинов и паролей на главную страницу.
                    self.parent.passwordsTable.setRowCount(len(self.passwords_data))
                    self.parent.passwordsTable.setColumnCount(len(self.passwords_data[0]))
                    for i, key in enumerate(self.passwords_data):
                        for j, item in enumerate(key):
                            new_item = QTableWidgetItem(str(item))
                            new_item.setFlags(QtCore.Qt.ItemIsEnabled)
                            self.parent.passwordsTable.setItem(i, j, new_item)

                    # Установка названий столбцов, а также столбцы расстягиваются по ширине QTableWidget.
                    self.parent.passwordsTable.setHorizontalHeaderLabels(KEYS)
                    header = self.parent.passwordsTable.horizontalHeader()
                    header.setSectionResizeMode(0, QHeaderView.Stretch)
                    header.setSectionResizeMode(1, QHeaderView.Stretch)
                    header.setSectionResizeMode(2, QHeaderView.Stretch)

                # После вывода окно добавления закрывается.
                self.close()
        except Exception as error:
            return error

    # Функция генерации пароля.
    def generate_password(self):
        try:
            # Проверка на то, хочет ли пользователь сгенерировтаь пароль.
            if self.generationPasswordCheckBox.checkState():
                length = 0
                special_symbols = self.specialSymbolsCheckBox.checkState()
                numbers = self.numbersCheckBox.checkState()
                # Проверки на случай того, если поле длины пароля пустое или в нем присутствуют другие символы, кроме чисел.
                if self.lengthPasswordLine.text() == "":
                    self.statusBar.showMessage("Вы не указали длину пароля")
                elif not self.lengthPasswordLine.text().isdigit():
                    self.statusBar.showMessage("Введите длину пароля числом")

                # Проверки на случай того, если пользователь введет длину меньше 8 или больше 64 символов.
                elif int(self.lengthPasswordLine.text()) < 8:
                    self.statusBar.showMessage("Длина пароля минимум 8 символов")
                elif int(self.lengthPasswordLine.text()) > 32:
                    self.statusBar.showMessage("Длина пароля не более 32 символов")
                else:
                    length = int(self.lengthPasswordLine.text())
                # Генерация пароля и вывод его в поле ввода.
                generator = PasswordGenerator(special_symbols, numbers, length)
                self.passwordLine.setText(generator.generate())
        except Exception as error:
            return error

    # После закрытия окна все поля очищаются, виджеты для генерации пароля скрываются.
    # Поле ввода пароля разблокируется.
    def closeEvent(self, event):
        try:
            self.serviceLine.setText("")
            self.loginLine.setText("")
            self.passwordLine.setText("")
            self.lengthPasswordLine.setText("")
            self.statusBar.showMessage("")

            self.specialSymbolsCheckBox.hide()
            self.numbersCheckBox.hide()
            self.lengthPasswordLabel.hide()
            self.lengthPasswordLine.hide()
            self.generateButton.hide()

            self.specialSymbolsCheckBox.setCheckState(False)
            self.numbersCheckBox.setCheckState(False)
            self.generationPasswordCheckBox.setCheckState(False)

            self.passwordLine.setReadOnly(False)
        except Exception as error:
            return error

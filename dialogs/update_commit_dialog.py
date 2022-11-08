from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore

from py_ui.update_commit_UI import Ui_Dialog
from database.database import DataBase
from constants import KEYS


# Диалогове окно для подтверждения редактирования.
class UpdateDialogCommit(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super(UpdateDialogCommit, self).__init__(parent)
        self.parent = parent
        self.setModal(True)
        self.setupUi(self)
        self.initUi()
        self.database = DataBase('./users.sqlite')

    def initUi(self):
        try:
            # Подключение функций для кнопок.
            self.noUpdateButton.clicked.connect(self.close_dialog)
            self.yesUpdateButton.clicked.connect(self.update_data)
        except Exception as error:
            return error

    # Функция вывода окна.
    def show_update_dialog_commit(self):
        try:
            self.show()
        except Exception as error:
            return error

    # Функция для обновления данных и их вывода.
    def update_data(self):
        try:
            data = self.database.select_all_for_check(self.parent.service, self.parent.login, self.parent.login_by_id)
            # Проверка существования данных аккаунта.
            if data:
                check = self.database.select_password_for_check_update(self.parent.service, self.parent.login,
                                                                       self.parent.password, self.parent.login_by_id)
                # Проверка на существование записи пароля в базе данных.
                if check:
                    self.close()
                    self.parent.statusBar.showMessage("Нельзя поменять пароль на такой же")
                else:
                    self.database.update_password(self.parent.service, self.parent.login,
                                                  self.parent.password, self.parent.login_by_id)
                    self.passwords_data = self.database.select_all_passwords(self.parent.login_by_id)
                    if self.passwords_data:
                        self.parent.main_table_widget.setRowCount(len(self.passwords_data))
                        self.parent.main_table_widget.setColumnCount(len(self.passwords_data[0]))
                        for i, key in enumerate(self.passwords_data):
                            for j, item in enumerate(key):
                                new_item = QTableWidgetItem(str(item))
                                new_item.setFlags(QtCore.Qt.ItemIsEnabled)
                                self.parent.main_table_widget.setItem(i, j, new_item)
                        self.parent.main_table_widget.setHorizontalHeaderLabels(KEYS)
                        header = self.parent.main_table_widget.horizontalHeader()
                        header.setSectionResizeMode(0, QHeaderView.Stretch)
                        header.setSectionResizeMode(1, QHeaderView.Stretch)
                        header.setSectionResizeMode(2, QHeaderView.Stretch)
                    self.close()
                    self.parent.close()
        except Exception as error:
            return error

    # Функция для закрытия окна.
    def close_dialog(self):
        try:
            self.close()
            self.parent.close()
        except Exception as error:
            return error

    # Очистка всех полей, после закрытия окна.
    def closeEvent(self, event):
        self.parent.serviceUpdateLine.setText("")
        self.parent.loginUpdateLine.setText("")
        self.parent.passwordUpdateLine.setText("")
        self.parent.statusBar.showMessage("")
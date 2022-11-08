from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore

from py_ui.delete_commit_UI import Ui_Dialog
from database.database import DataBase
from constants import KEYS


# Окно подтверждения удаления.
class DeleteCommitDialog(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super(DeleteCommitDialog, self).__init__(parent)
        self.parent = parent
        self.setModal(True)
        self.setupUi(self)
        self.initUi()
        self.database = DataBase("./users.sqlite")

    def initUi(self):
        try:
            # Подключение функций для кнопок.
            self.yesButton.clicked.connect(self.delete)
            self.noButton.clicked.connect(self.close_dialog)
        except Exception as error:
            return error

    # Функция для появления окна.
    def show_delete_commit_dialog(self):
        try:
            self.show()
        except Exception as error:
            return error

    # Функция удаления
    def delete(self):
        try:
            data = self.database.select_all_for_check(self.parent.service, self.parent.login, self.parent.login_by_id)
            # Проверка на наличие логина и пароля.
            if data:
                self.database.delete_password(self.parent.service, self.parent.login, self.parent.login_by_id)
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
                else:
                    self.parent.main_table_widget.setRowCount(0)
                    self.parent.main_table_widget.setColumnCount(0)
                self.close()
                self.parent.close()

            else:
                self.parent.statusBar.showMessage('Логин и пароль не были найдены')
                self.close()
        except Exception as error:
            return error

    # Функция для закрытия окна
    def close_dialog(self):
        try:
            self.close()
            self.parent.close()
        except Exception as error:
            return error

    # Очистка всех полей ввода, после закрытия.
    def closeEvent(self, event):
        try:
            self.parent.serviceLine.setText("")
            self.parent.loginLine.setText("")
            self.parent.statusBar.showMessage("")
        except Exception as error:
            return error

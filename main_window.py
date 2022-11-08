from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QStatusBar
from PyQt5 import QtCore

from database.database import DataBase
from py_ui import main_UI

from dialogs.start_dialog import StartDialog
from dialogs.add_dialog import AddDialog
from dialogs.delete_dialog import DeleteDialog
from dialogs.update_dialog import UpdateDialog
from dialogs.export_commit_dialog import ExportCommitDialog
from dialogs.export_error_dialog import ExportErrorDialog

from functions.exporter import Exporter


# Класс центрального виджета.
class QtPasswordManager(QWidget, main_UI.Ui_Form):
    def __init__(self, parent=None):
        super(QtPasswordManager, self).__init__(parent)
        self.parent = parent
        self.database = DataBase('./users.sqlite')
        self.setupUi(self)

        # Подключение различных диалоговых окон для работы с ними.
        self.start_dialog = StartDialog(self.parent)
        self.start_dialog.show()
        self.add_dialog = AddDialog(self)
        self.delete_dialog = DeleteDialog(self)
        self.update_dialog = UpdateDialog(self)
        self.export_commit_dialog = ExportCommitDialog(self)
        self.export_error_dialog = ExportErrorDialog(self)

        self.initUi()

    def initUi(self):
        try:
            # Установка изображения.
            self.pixmap = QPixmap("img/happy birthday.png").scaled(336, 867, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap)

            # Подключение функций для кнопок на главном окне.
            self.addButton.clicked.connect(self.add_dialog.show_add_logins_dialog)
            self.deleteButton.clicked.connect(self.delete_dialog.show_delete_logins_dialog)
            self.editButton.clicked.connect(self.update_dialog.show_update_logins_dialog)
            self.exportButton.clicked.connect(self.export)
        except Exception as error:
            return error

    # Функция для экспорта паролей
    def export(self):
        try:
            login = self.start_dialog.login.text()

            # Передаем название файла и логин пользователя для экспорта.
            export_method = Exporter('./logins.csv', login)
            check = export_method.export_to_csv()

            # Проверка на успешность выполнения экспорта.
            # type(check) используется, чтобы при возвращении ошибки не вышло окно о том, что все прошло успешно.
            if type(check) is bool and check:
                self.export_commit_dialog.show()
            else:
                self.export_error_dialog.exportErrorLabel.setText("Невозможно экспортировать.\n"
                                                                  f"Причина: {check}")
                self.export_error_dialog.show()

        except Exception as error:
            self.export_error_dialog.exportErrorLabel.setText("Невозможно экспортировать.\n"
                                                              f"Причина: {error}")
            return error

    # Функция для появления стартового диалогового окна при запуске программы.
    def create_dialog(self):
        try:
            self.start_dialog.show()
        except Exception as error:
            return error

from PyQt5.QtWidgets import QDialog, QStatusBar

from py_ui.delete_UI import Ui_Dialog
from dialogs.delete_commit_dialog import DeleteCommitDialog


# Диалоговое окно для удаления паролей.
class DeleteDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(DeleteDialog, self).__init__(parent)
        self.parent = parent
        self.setModal(True)
        self.statusBar = QStatusBar(self)
        self.statusBar.move(4, 0)
        self.statusBar.resize(400, 15)
        self.setupUi(self)
        self.delete_commit = DeleteCommitDialog(self)
        self.initUi()
        self.main_table_widget = self.parent.passwordsTable

    def initUi(self):
        try:
            # Подключение функции для кнопки.
            self.commitButton.clicked.connect(self.delete_logins)
        except Exception as error:
            return error

    # Функция для того, чтобы окно появилось.
    def show_delete_logins_dialog(self):
        try:
            self.show()
        except Exception as error:
            return error

    # Функция удаления.
    def delete_logins(self):
        try:
            self.service = self.serviceLine.text()
            self.login = self.loginLine.text()
            self.login_by_id = self.parent.start_dialog.login.text()

            # Проверки на случай того, если поля пустые.
            if self.service == "":
                self.statusBar.showMessage('Вы не указали сервис')
            elif self.login == "":
                self.statusBar.showMessage('Вы не указали логин')
            else:
                # Вывод окна для подтверждения удаления.
                self.delete_commit.show_delete_commit_dialog()
        except Exception as error:
            return error

    # После закрытия окна все поля очищаются.
    def closeEvent(self, event):
        try:
            self.serviceLine.setText("")
            self.loginLine.setText("")
            self.statusBar.showMessage("")
        except Exception as error:
            return error
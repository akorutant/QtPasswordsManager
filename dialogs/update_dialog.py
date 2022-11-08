from PyQt5.QtWidgets import QDialog, QStatusBar

from database.database import DataBase
from py_ui.update_dialog_UI import Ui_Dialog
from dialogs.update_commit_dialog import UpdateDialogCommit
from functions.password_generator import PasswordGenerator


# Диалоговое окно для обновления пароля.
class UpdateDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(UpdateDialog, self).__init__(parent)
        self.parent = parent
        self.setModal(True)
        self.statusBar = QStatusBar(self)
        self.statusBar.move(4, 0)
        self.statusBar.resize(421, 15)
        self.setupUi(self)
        self.database = DataBase('./users.sqlite')
        self.update_dialog_commit = UpdateDialogCommit(self)
        self.initUi()
        self.main_table_widget = self.parent.passwordsTable

    def initUi(self):
        try:
            # Подключение функций для кнопок.
            self.generateUpdatePasswordCheckBox.clicked.connect(self.check_state)
            self.commitUpdateButton.clicked.connect(self.update_password)
            self.generateUpdateButton.clicked.connect(self.generate_password)

            # Скрываются виджеты, которые должны появится только, если пользовтаель хочет сгенерировать пароль.
            self.specialSymbolsUpdateCheckBox.hide()
            self.numbersUpdateCheckBox.hide()
            self.lengthUpdatePasswordLine.hide()
            self.lengthUpdatePasswordLabel.hide()
            self.generateUpdateButton.hide()
        except Exception as error:
            return error

    # Функция для вывода окна.
    def show_update_logins_dialog(self):
        try:
            self.show()
        except Exception as error:
            return error

    # Проверка, хочет ли пользователь сгенерировать пароль.
    def check_state(self):
        try:
            # Если пользователь хочет сгенерировать пароль, то появлются нужные виджеты.
            # Поле ввода пароля блокируется для редактирования.
            if self.generateUpdatePasswordCheckBox.checkState():
                self.specialSymbolsUpdateCheckBox.show()
                self.numbersUpdateCheckBox.show()
                self.lengthUpdatePasswordLabel.show()
                self.generateUpdateButton.show()
                self.lengthUpdatePasswordLine.show()
                self.passwordUpdateLine.setReadOnly(True)

            # Если пользователь передумал генерировать пароль, то виджеты скрываются.
            # Поле ввода пароля разблокируется.
            else:
                self.specialSymbolsUpdateCheckBox.hide()
                self.numbersUpdateCheckBox.hide()
                self.lengthUpdatePasswordLabel.hide()
                self.lengthUpdatePasswordLabel.hide()
                self.generateUpdateButton.hide()
                self.passwordUpdateLine.setReadOnly(False)
        except Exception as error:
            return error

    # Функция обновления пароля.
    def update_password(self):
        try:
            self.service = self.serviceUpdateLine.text().lower()
            self.login = self.loginUpdateLine.text()
            self.password = self.passwordUpdateLine.text()
            self.login_by_id = self.parent.start_dialog.login.text()
            data = self.database.select_all_for_check(self.service, self.login, self.login_by_id)

            # Проверки, если поля пустые.
            if data and self.password != "":
                self.update_dialog_commit.show_update_dialog_commit()
            elif self.service == "":
                self.statusBar.showMessage('Вы не указали сервис')
            elif self.login == "":
                self.statusBar.showMessage("Вы не указали логин")
            elif self.password == "":
                self.statusBar.showMessage("Вы не указали пароль")
            else:
                self.statusBar.showMessage("Такого логина не найдено")
        except Exception as error:
            return error

    # Функция генерации пароля.
    def generate_password(self):
        try:
            if self.generateUpdatePasswordCheckBox.checkState():
                length = 0
                special_symbols = self.specialSymbolsUpdateCheckBox.checkState()
                numbers = self.numbersUpdateCheckBox.checkState()

                # Проверки на случай того, если поле длины пароля пустое или в нем присутствуют другие символы, кроме чисел.
                if self.lengthUpdatePasswordLine.text() == "":
                    self.statusBar.showMessage("Вы не указали длину пароля")
                elif not self.lengthUpdatePasswordLine.text().isdigit():
                    self.statusBar.showMessage("Укажите длину пароля числом")

                # Проверки на случай того, если пользователь введет длину меньше 8 или больше 64 символов.
                elif int(self.lengthUpdatePasswordLine.text()) < 8:
                    self.statusBar.showMessage("Длина пароля минимум 8 символов")
                elif int(self.lengthUpdatePasswordLine.text()) > 32:
                    self.statusBar.showMessage("Длина пароля не более 32 символов")
                else:
                    # Генерация пароля и вывод его в поле ввода.
                    length = int(self.lengthUpdatePasswordLine.text())
                    generator = PasswordGenerator(special_symbols, numbers, length)
                    self.passwordUpdateLine.setText(generator.generate())
        except Exception as error:
            return error

    # После закрытия окна все поля очищаются, виджеты для генерации пароля скрываются.
    # Поле ввода пароля разблокируется.
    def closeEvent(self, event):
        try:
            self.serviceUpdateLine.setText("")
            self.loginUpdateLine.setText("")
            self.passwordUpdateLine.setText("")
            self.lengthUpdatePasswordLine.setText("")

            self.statusBar.showMessage("")

            self.specialSymbolsUpdateCheckBox.setCheckState(False)
            self.numbersUpdateCheckBox.setCheckState(False)
            self.generateUpdatePasswordCheckBox.setCheckState(False)

            self.specialSymbolsUpdateCheckBox.hide()
            self.numbersUpdateCheckBox.hide()
            self.lengthUpdatePasswordLabel.hide()
            self.lengthUpdatePasswordLabel.hide()
            self.generateUpdateButton.hide()

            self.passwordUpdateLine.setReadOnly(False)
        except Exception as error:
            return error
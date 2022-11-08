import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from database.database import DataBase
from main_window import QtPasswordManager


# Класс главного окна.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Passwords Manager')
        self.setGeometry(500, 100, 911, 787)

        # Установка центрального виджета на главном окне, как основной дизайн всей программы.
        # Родительским окном для QtPasswordManager будет класс MainWindow
        self.central_widget = QtPasswordManager(self)
        self.setCentralWidget(self.central_widget)
        self.central_widget.create_dialog()

    # После закрытия программы происходит отключение от базы данных.
    def closeEvent(self, event):
        database.close_database()


def except_hook(c, e, t):
    return sys.__excepthook__(c, e, t)


if __name__ == "__main__":
    database = DataBase('./users.sqlite')
    database.create_database()
    app = QApplication(sys.argv)
    program = MainWindow()
    sys.excepthook = except_hook
    sys.exit(app.exec())

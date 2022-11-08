from PyQt5.QtWidgets import QDialog

from py_ui.export_error_UI import Ui_Dialog


# Диалоговое окно для информаирования об ошибке экспорта.
class ExportErrorDialog(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super(ExportErrorDialog, self).__init__(parent)
        self.parent = parent
        self.setModal(True)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.okErrorButton.clicked.connect(self.close)
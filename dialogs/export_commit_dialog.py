from PyQt5.QtWidgets import QDialog

from py_ui.export_commit_UI import Ui_Dialog


# Диалоговое окно для информаирования об успешности экспорта.
class ExportCommitDialog(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super(ExportCommitDialog, self).__init__(parent)
        self.parent = parent
        self.setModal(True)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.okButton.clicked.connect(self.close)
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_commit_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 115)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.yesUpdateButton = QtWidgets.QPushButton(Dialog)
        self.yesUpdateButton.setObjectName("yesUpdateButton")
        self.gridLayout_2.addWidget(self.yesUpdateButton, 1, 0, 1, 1)
        self.noUpdateButton = QtWidgets.QPushButton(Dialog)
        self.noUpdateButton.setObjectName("noUpdateButton")
        self.gridLayout_2.addWidget(self.noUpdateButton, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Подтвердите действие"))
        self.yesUpdateButton.setText(_translate("Dialog", "Да"))
        self.noUpdateButton.setText(_translate("Dialog", "Нет"))
        self.label.setText(_translate("Dialog", "Вы уверены что хотите обновить?"))

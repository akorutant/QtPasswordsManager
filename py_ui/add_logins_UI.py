# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_logins_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QDialog(object):
    def setupUi(self, QDialog):
        QDialog.setObjectName("QDialog")
        QDialog.resize(294, 302)
        QDialog.setMaximumSize(QtCore.QSize(294, 302))
        self.gridLayout_2 = QtWidgets.QGridLayout(QDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(QDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.serviceLine = QtWidgets.QLineEdit(QDialog)
        self.serviceLine.setObjectName("serviceLine")
        self.verticalLayout.addWidget(self.serviceLine)
        self.label_2 = QtWidgets.QLabel(QDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.loginLine = QtWidgets.QLineEdit(QDialog)
        self.loginLine.setObjectName("loginLine")
        self.verticalLayout.addWidget(self.loginLine)
        self.label_3 = QtWidgets.QLabel(QDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.passwordLine = QtWidgets.QLineEdit(QDialog)
        self.passwordLine.setObjectName("passwordLine")
        self.verticalLayout.addWidget(self.passwordLine)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commitButton = QtWidgets.QPushButton(QDialog)
        self.commitButton.setObjectName("commitButton")
        self.horizontalLayout.addWidget(self.commitButton)
        self.generateButton = QtWidgets.QPushButton(QDialog)
        self.generateButton.setObjectName("generateButton")
        self.horizontalLayout.addWidget(self.generateButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 7, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.generationPasswordCheckBox = QtWidgets.QCheckBox(QDialog)
        self.generationPasswordCheckBox.setEnabled(True)
        self.generationPasswordCheckBox.setObjectName("generationPasswordCheckBox")
        self.verticalLayout_3.addWidget(self.generationPasswordCheckBox)
        self.specialSymbolsCheckBox = QtWidgets.QCheckBox(QDialog)
        self.specialSymbolsCheckBox.setEnabled(True)
        self.specialSymbolsCheckBox.setObjectName("specialSymbolsCheckBox")
        self.verticalLayout_3.addWidget(self.specialSymbolsCheckBox)
        self.numbersCheckBox = QtWidgets.QCheckBox(QDialog)
        self.numbersCheckBox.setEnabled(True)
        self.numbersCheckBox.setObjectName("numbersCheckBox")
        self.verticalLayout_3.addWidget(self.numbersCheckBox)
        self.lengthPasswordLabel = QtWidgets.QLabel(QDialog)
        self.lengthPasswordLabel.setEnabled(True)
        self.lengthPasswordLabel.setObjectName("lengthPasswordLabel")
        self.verticalLayout_3.addWidget(self.lengthPasswordLabel)
        self.lengthPasswordLine = QtWidgets.QLineEdit(QDialog)
        self.lengthPasswordLine.setEnabled(True)
        self.lengthPasswordLine.setObjectName("lengthPasswordLine")
        self.verticalLayout_3.addWidget(self.lengthPasswordLine)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.retranslateUi(QDialog)
        QtCore.QMetaObject.connectSlotsByName(QDialog)

    def retranslateUi(self, QDialog):
        _translate = QtCore.QCoreApplication.translate
        QDialog.setWindowTitle(_translate("QDialog", "Введите данные"))
        self.label.setText(_translate("QDialog", "Сервис"))
        self.label_2.setText(_translate("QDialog", "Логин"))
        self.label_3.setText(_translate("QDialog", "Пароль"))
        self.commitButton.setText(_translate("QDialog", "Подтвердить"))
        self.generateButton.setText(_translate("QDialog", "Сгенерировать"))
        self.generationPasswordCheckBox.setText(_translate("QDialog", "Сгенерировать пароль"))
        self.specialSymbolsCheckBox.setText(_translate("QDialog", "Специальные символы"))
        self.numbersCheckBox.setText(_translate("QDialog", "Цифры"))
        self.lengthPasswordLabel.setText(_translate("QDialog", "Длина пароля (От 8 до 32):"))

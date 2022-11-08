# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(911, 787)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setObjectName("mainTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.mainTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.buttonsLayout = QtWidgets.QVBoxLayout()
        self.buttonsLayout.setContentsMargins(-1, 0, -1, -1)
        self.buttonsLayout.setObjectName("buttonsLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.buttonsLayout.addItem(spacerItem)
        self.exportButton = QtWidgets.QPushButton(self.mainTab)
        self.exportButton.setObjectName("exportButton")
        self.buttonsLayout.addWidget(self.exportButton)
        self.addButton = QtWidgets.QPushButton(self.mainTab)
        self.addButton.setObjectName("addButton")
        self.buttonsLayout.addWidget(self.addButton)
        self.editButton = QtWidgets.QPushButton(self.mainTab)
        self.editButton.setObjectName("editButton")
        self.buttonsLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(self.mainTab)
        self.deleteButton.setObjectName("deleteButton")
        self.buttonsLayout.addWidget(self.deleteButton)
        self.gridLayout_3.addLayout(self.buttonsLayout, 0, 0, 1, 1)
        self.listLayout = QtWidgets.QVBoxLayout()
        self.listLayout.setObjectName("listLayout")
        self.passwordsTable = QtWidgets.QTableWidget(self.mainTab)
        self.passwordsTable.setObjectName("passwordsTable")
        self.passwordsTable.setColumnCount(0)
        self.passwordsTable.setRowCount(0)
        self.listLayout.addWidget(self.passwordsTable)
        self.gridLayout_3.addLayout(self.listLayout, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 5)
        self.tabWidget.addTab(self.mainTab, "")
        self.helpTab = QtWidgets.QWidget()
        self.helpTab.setObjectName("helpTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.helpTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.helpTab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.helpTab)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.helpTab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.helpTab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.image = QtWidgets.QLabel(self.helpTab)
        self.image.setText("")
        self.image.setObjectName("image")
        self.verticalLayout.addWidget(self.image)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.helpTab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.exportButton.setText(_translate("Form", "Экспортировать"))
        self.addButton.setText(_translate("Form", "Добавить"))
        self.editButton.setText(_translate("Form", "Редактировать"))
        self.deleteButton.setText(_translate("Form", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), _translate("Form", "Главная"))
        self.label_2.setText(_translate("Form", "Кнопка \"Добавить\" - используется для добавления логина и пароля."))
        self.label.setText(_translate("Form", "Кнопка \"Редактировать\" - используется для изменения вашего пароля."))
        self.label_5.setText(_translate("Form", "Кнопка \"Экспортировать\" - используется для экспорта ваших логинов и паролей в csv файл."))
        self.label_3.setText(_translate("Form", "Кнопка \"Удалить\" - используется для удаления логина и пароля."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.helpTab), _translate("Form", "Помощь"))

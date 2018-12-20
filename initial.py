# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'initial.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Initial(object):
    def setupUi(self, Initial):
        Initial.setObjectName("Initial")
        Initial.resize(609, 407)
        self.centralwidget = QtWidgets.QWidget(Initial)
        self.centralwidget.setObjectName("centralwidget")
        self.listTodo = QtWidgets.QComboBox(self.centralwidget)
        self.listTodo.setGeometry(QtCore.QRect(40, 60, 171, 41))
        self.listTodo.setObjectName("listTodo")
        self.newTodoButtom = QtWidgets.QPushButton(self.centralwidget)
        self.newTodoButtom.setGeometry(QtCore.QRect(290, 40, 241, 71))
        self.newTodoButtom.setObjectName("newTodoButtom")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 171, 31))
        self.label.setObjectName("label")
        self.openTodoButtom = QtWidgets.QPushButton(self.centralwidget)
        self.openTodoButtom.setGeometry(QtCore.QRect(40, 140, 171, 61))
        self.openTodoButtom.setObjectName("openTodoButtom")
        Initial.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Initial)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 18))
        self.menubar.setObjectName("menubar")
        Initial.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Initial)
        self.statusbar.setObjectName("statusbar")
        Initial.setStatusBar(self.statusbar)

        self.retranslateUi(Initial)
        QtCore.QMetaObject.connectSlotsByName(Initial)

    def retranslateUi(self, Initial):
        _translate = QtCore.QCoreApplication.translate
        Initial.setWindowTitle(_translate("Initial", "MainWindow"))
        self.newTodoButtom.setText(_translate("Initial", "Создать новую заметку"))
        self.label.setText(
            _translate("Initial", "<html><head/><body><p align=\"center\">Выберите заметку</p></body></html>"))
        self.openTodoButtom.setText(_translate("Initial", "Открыть заметку"))

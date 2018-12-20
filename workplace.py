# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workplace.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WorkPlace(object):
    def setupUi(self, WorkPlace):
        WorkPlace.setObjectName("WorkPlace")
        WorkPlace.resize(794, 594)
        self.centralwidget = QtWidgets.QWidget(WorkPlace)
        self.centralwidget.setObjectName("centralwidget")
        self.TextBlock = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.TextBlock.setGeometry(QtCore.QRect(10, 10, 771, 551))
        self.TextBlock.setObjectName("TextBlock")
        WorkPlace.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WorkPlace)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 18))
        self.menubar.setObjectName("menubar")
        WorkPlace.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WorkPlace)
        self.statusbar.setObjectName("statusbar")
        WorkPlace.setStatusBar(self.statusbar)

        self.retranslateUi(WorkPlace)
        QtCore.QMetaObject.connectSlotsByName(WorkPlace)

    def retranslateUi(self, WorkPlace):
        _translate = QtCore.QCoreApplication.translate
        WorkPlace.setWindowTitle(_translate("WorkPlace", "MainWindow"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_qMainWindow(object):
    def setupUi(self, qMainWindow):
        qMainWindow.setObjectName("qMainWindow")
        qMainWindow.resize(1082, 780)
        self.centralwidget = QtWidgets.QWidget(qMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(40, 80, 591, 561))
        self.openGLWidget.setObjectName("openGLWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(710, 90, 41, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(710, 130, 41, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(780, 90, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(780, 130, 221, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 180, 71, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(930, 180, 71, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(710, 340, 291, 301))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(710, 300, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(710, 240, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(830, 240, 111, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 680, 591, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        qMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(qMainWindow)
        self.statusbar.setObjectName("statusbar")
        qMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(qMainWindow)
        QtCore.QMetaObject.connectSlotsByName(qMainWindow)

    def retranslateUi(self, qMainWindow):
        _translate = QtCore.QCoreApplication.translate
        qMainWindow.setWindowTitle(_translate("qMainWindow", "Manaka_Nemu"))
        self.label.setText(_translate("qMainWindow", "IP:"))
        self.label_2.setText(_translate("qMainWindow", "Port:"))
        self.pushButton.setText(_translate("qMainWindow", "Connect"))
        self.pushButton_2.setText(_translate("qMainWindow", "Close"))
        self.label_3.setText(_translate("qMainWindow", "Log:"))
        self.label_4.setText(_translate("qMainWindow", "Status:"))
        self.label_5.setText(_translate("qMainWindow", "Default"))
        self.pushButton_3.setText(_translate("qMainWindow", "Draw"))


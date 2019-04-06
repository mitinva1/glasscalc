# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glasscalc.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GlassCalc1(object):
    def setupUi(self, GlassCalc1):
        GlassCalc1.setObjectName("GlassCalc1")
        GlassCalc1.resize(459, 216)
        self.centralwidget = QtWidgets.QWidget(GlassCalc1)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 201, 101))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 40, 201, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        GlassCalc1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GlassCalc1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        self.menubar.setObjectName("menubar")
        GlassCalc1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GlassCalc1)
        self.statusbar.setObjectName("statusbar")
        GlassCalc1.setStatusBar(self.statusbar)

        self.retranslateUi(GlassCalc1)
        QtCore.QMetaObject.connectSlotsByName(GlassCalc1)

    def retranslateUi(self, GlassCalc1):
        _translate = QtCore.QCoreApplication.translate
        GlassCalc1.setWindowTitle(_translate("GlassCalc1", "glasscalc1"))
        self.pushButton.setText(_translate("GlassCalc1", "Двари \"классика\" "))
        self.label.setText(_translate("GlassCalc1", "Выбор системы для расчета"))
        self.pushButton_2.setText(_translate("GlassCalc1", "душевая "))



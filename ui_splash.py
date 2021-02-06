# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashHSrwvf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_splashScreen(object):
    def setupUi(self, splashScreen):
        if not splashScreen.objectName():
            splashScreen.setObjectName(u"splashScreen")
        splashScreen.resize(680, 400)
        self.centralwidget = QWidget(splashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 80, 661, 71))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 160, 661, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(80, 250, 521, 25))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color:rgb(200, 200, 200);\n"
"	border-style:none;\n"
"	border-radius:10px;\n"
"	text-align:center;	\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511, x2:1, y2:0.523, stop:0 rgba(254, 121, 189, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 290, 661, 51))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(10, 340, 641, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_status = QLabel(self.dropShadowFrame)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(0, 200, 661, 31))
        self.label_status.setFont(font1)
        self.label_status.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_status.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        splashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(splashScreen)

        QMetaObject.connectSlotsByName(splashScreen)
    # setupUi

    def retranslateUi(self, splashScreen):
        splashScreen.setWindowTitle(QCoreApplication.translate("splashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("splashScreen", u"<html><head/><body><p><span style=\" font-weight:600;\">Covid </span>Dashboard</p></body></html>", None))
        self.label_description.setText(QCoreApplication.translate("splashScreen", u"<strong>Visualization</strong> Tool", None))
        self.label_loading.setText(QCoreApplication.translate("splashScreen", u"loading ...", None))
        self.label_credits.setText(QCoreApplication.translate("splashScreen", u"<strong>Created By</strong>: Group", None))
        self.label_status.setText(QCoreApplication.translate("splashScreen", u"<html><head/><body><p><span style=\" font-weight:600;\">Loading </span>status</p></body></html>", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startupDialogellKqn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_welcomeDialog(object):
    def setupUi(self, welcomeDialog):
        if not welcomeDialog.objectName():
            welcomeDialog.setObjectName(u"welcomeDialog")
        welcomeDialog.resize(600, 400)
        welcomeDialog.setStyleSheet(u"background-color: rgb(22, 25, 37);")
        self.gridLayout = QGridLayout(welcomeDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_title = QLabel(welcomeDialog)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(18)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"margin-top:10px;\n"
"margin-bottom:10px;")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_title, 1, 0, 1, 1, Qt.AlignTop)

        self.label_openRecent = QLabel(welcomeDialog)
        self.label_openRecent.setObjectName(u"label_openRecent")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_openRecent.setFont(font1)
        self.label_openRecent.setStyleSheet(u"margin-left:20px;")
        self.label_openRecent.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_openRecent, 2, 0, 1, 1)

        self.openRecentList = QListView(welcomeDialog)
        self.openRecentList.setObjectName(u"openRecentList")
        self.openRecentList.setStyleSheet(u"QListView{background: transparent;  border:none; }")

        self.gridLayout.addWidget(self.openRecentList, 5, 0, 4, 1)

        self.label_samples = QLabel(welcomeDialog)
        self.label_samples.setObjectName(u"label_samples")
        self.label_samples.setFont(font1)
        self.label_samples.setStyleSheet(u"margin-left:20px;")
        self.label_samples.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_samples.setMargin(0)

        self.gridLayout.addWidget(self.label_samples, 7, 1, 1, 1)

        self.samplesList = QListView(welcomeDialog)
        self.samplesList.setObjectName(u"samplesList")
        self.samplesList.setStyleSheet(u"QListView{\n"
"	background: transparent;\n"
"	 border:none ;\n"
"}")
        self.samplesList.setItemAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.samplesList, 8, 1, 1, 1)

        self.label_newProject = QLabel(welcomeDialog)
        self.label_newProject.setObjectName(u"label_newProject")
        self.label_newProject.setFont(font1)
        self.label_newProject.setStyleSheet(u"margin-left:20px;")
        self.label_newProject.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_newProject, 2, 1, 1, 1)

        self.startupCheckbox = QCheckBox(welcomeDialog)
        self.startupCheckbox.setObjectName(u"startupCheckbox")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.startupCheckbox.setFont(font2)
        self.startupCheckbox.setChecked(True)

        self.gridLayout.addWidget(self.startupCheckbox, 9, 0, 1, 1)

        self.newhorizontal = QHBoxLayout()
        self.newhorizontal.setObjectName(u"newhorizontal")
        self.newhorizontal.setContentsMargins(20, -1, -1, -1)
        self.newfilebtn = QPushButton(welcomeDialog)
        self.newfilebtn.setObjectName(u"newfilebtn")
        self.newfilebtn.setMaximumSize(QSize(101, 16777215))
        self.newfilebtn.setStyleSheet(u"color:rgb(85, 170, 255);")
        self.newfilebtn.setAutoDefault(False)
        self.newfilebtn.setFlat(True)

        self.newhorizontal.addWidget(self.newfilebtn, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.newhorizontal.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.newhorizontal, 5, 1, 1, 1)


        self.retranslateUi(welcomeDialog)

        QMetaObject.connectSlotsByName(welcomeDialog)
    # setupUi

    def retranslateUi(self, welcomeDialog):
        welcomeDialog.setWindowTitle(QCoreApplication.translate("welcomeDialog", u"Dialog", None))
        self.label_title.setText(QCoreApplication.translate("welcomeDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Welcome</span> to Covid Dashboard</p></body></html>", None))
        self.label_openRecent.setText(QCoreApplication.translate("welcomeDialog", u"Open recent", None))
        self.label_samples.setText(QCoreApplication.translate("welcomeDialog", u"Samples", None))
        self.label_newProject.setText(QCoreApplication.translate("welcomeDialog", u"New Project", None))
#if QT_CONFIG(tooltip)
        self.startupCheckbox.setToolTip(QCoreApplication.translate("welcomeDialog", u"<html><head/><body><p>Open at Startup</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.startupCheckbox.setText(QCoreApplication.translate("welcomeDialog", u"Open at startup", None))
#if QT_CONFIG(tooltip)
        self.newfilebtn.setToolTip(QCoreApplication.translate("welcomeDialog", u"<html><head/><body><p>Open New File</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.newfilebtn.setText(QCoreApplication.translate("welcomeDialog", u"New File", None))
    # retranslateUi


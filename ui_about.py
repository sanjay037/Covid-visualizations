# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutNkMYri.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(578, 385)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutDialog.sizePolicy().hasHeightForWidth())
        AboutDialog.setSizePolicy(sizePolicy)
        AboutDialog.setStyleSheet(u"background-color: rgb(22, 24, 34);")
        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.about = QLabel(AboutDialog)
        self.about.setObjectName(u"about")
        self.about.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.about)


        self.retranslateUi(AboutDialog)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        AboutDialog.setToolTip(QCoreApplication.translate("AboutDialog", u"About", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        AboutDialog.setStatusTip(QCoreApplication.translate("AboutDialog", u"About", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        AboutDialog.setWhatsThis(QCoreApplication.translate("AboutDialog", u"About the Application", None))
#endif // QT_CONFIG(whatsthis)
        self.about.setText(QCoreApplication.translate("AboutDialog", u"<html><head/><body><p align=\"center\">Made as part of <span style=\" font-weight:600;\">Datathon 7</span></p><p align=\"center\"><span style=\" font-weight:600;\">GUI and DataViz Integration</span> Made by <span style=\" font-weight:600;\">Saikiran</span></p><p align=\"center\"><span style=\" font-weight:600;\">Network Plot </span>Made by <span style=\" font-weight:600;\">Sanjay</span></p><p align=\"center\"><span style=\" font-weight:600;\">ChoroPleth Plot </span>Made by <span style=\" font-weight:600;\">Khalid</span></p><p align=\"center\"><span style=\" font-weight:600;\">LineGraph and Data Preprocessing </span>Made by <span style=\" font-weight:600;\">Rohith</span></p><p align=\"center\"><span style=\" font-weight:600;\">Scatter Plot </span>Made by <span style=\" font-weight:600;\">Saikiran</span></p></body></html>", None))
    # retranslateUi


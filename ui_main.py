# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainmlTupi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet(u"background-color: rgb(23, 25, 35);")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit.setShortcutContext(Qt.WindowShortcut)
        self.actionExit.setPriority(QAction.HighPriority)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionShow_Startup_Dialog = QAction(MainWindow)
        self.actionShow_Startup_Dialog.setObjectName(u"actionShow_Startup_Dialog")
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionOpen_File.setShortcutContext(Qt.WindowShortcut)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setStyleSheet(u"background-color: rgb(41, 45, 62);")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setTabBarAutoHide(False)
        self.choropleth = QWidget()
        self.choropleth.setObjectName(u"choropleth")
        self.choropleth.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.choropleth)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.choroplethgridLayout = QGridLayout()
        self.choroplethgridLayout.setObjectName(u"choroplethgridLayout")

        self.horizontalLayout.addLayout(self.choroplethgridLayout)

        self.choroplothtoolBox = QToolBox(self.choropleth)
        self.choroplothtoolBox.setObjectName(u"choroplothtoolBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choroplothtoolBox.sizePolicy().hasHeightForWidth())
        self.choroplothtoolBox.setSizePolicy(sizePolicy)
        self.choroplothtoolBox.setMinimumSize(QSize(200, 0))
        self.choroplothtoolBox.setMaximumSize(QSize(250, 16777215))
        self.choroplothtoolBox.setStyleSheet(u"background-color: rgb(27, 30, 43);")
        self.choroControls = QWidget()
        self.choroControls.setObjectName(u"choroControls")
        self.choroControls.setGeometry(QRect(0, 0, 250, 617))
        self.formLayout_2 = QFormLayout(self.choroControls)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_5 = QLabel(self.choroControls)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.choroColumn = QComboBox(self.choroControls)
        self.choroColumn.setObjectName(u"choroColumn")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.choroColumn)

        self.label_8 = QLabel(self.choroControls)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMargin(20)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.choroPlotbtn = QPushButton(self.choroControls)
        self.choroPlotbtn.setObjectName(u"choroPlotbtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.choroPlotbtn.sizePolicy().hasHeightForWidth())
        self.choroPlotbtn.setSizePolicy(sizePolicy1)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.choroPlotbtn)

        self.choroplothtoolBox.addItem(self.choroControls, u"Controls")
        self.choroTools = QWidget()
        self.choroTools.setObjectName(u"choroTools")
        self.choroTools.setGeometry(QRect(0, 0, 250, 617))
        self.choroverticalLayout = QVBoxLayout(self.choroTools)
        self.choroverticalLayout.setObjectName(u"choroverticalLayout")
        self.choroverticalLayout.setContentsMargins(20, -1, 20, -1)
        self.choroexportbtn = QPushButton(self.choroTools)
        self.choroexportbtn.setObjectName(u"choroexportbtn")

        self.choroverticalLayout.addWidget(self.choroexportbtn)

        self.choroplothtoolBox.addItem(self.choroTools, u"Tools")

        self.horizontalLayout.addWidget(self.choroplothtoolBox)

        self.tabWidget.addTab(self.choropleth, "")
        self.network = QWidget()
        self.network.setObjectName(u"network")
        self.network.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.network)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.networkgridLayout = QGridLayout()
        self.networkgridLayout.setObjectName(u"networkgridLayout")

        self.horizontalLayout_2.addLayout(self.networkgridLayout)

        self.networkToolBox = QToolBox(self.network)
        self.networkToolBox.setObjectName(u"networkToolBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.networkToolBox.sizePolicy().hasHeightForWidth())
        self.networkToolBox.setSizePolicy(sizePolicy2)
        self.networkToolBox.setMinimumSize(QSize(450, 0))
        self.networkToolBox.setMaximumSize(QSize(450, 16777215))
        self.networkToolBox.setStyleSheet(u"background-color: rgb(27, 30, 43);")
        self.networkControls = QWidget()
        self.networkControls.setObjectName(u"networkControls")
        self.networkControls.setGeometry(QRect(0, 0, 450, 605))
        self.formLayout = QFormLayout(self.networkControls)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(12, -1, 24, -1)
        self.label = QLabel(self.networkControls)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label.setMargin(12)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.corrDir = QComboBox(self.networkControls)
        self.corrDir.addItem("")
        self.corrDir.addItem("")
        self.corrDir.setObjectName(u"corrDir")
        self.corrDir.setInsertPolicy(QComboBox.InsertAtBottom)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.corrDir)

        self.label_2 = QLabel(self.networkControls)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMargin(12)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.corrVal = QSlider(self.networkControls)
        self.corrVal.setObjectName(u"corrVal")
        self.corrVal.setStyleSheet(u"margin-top:33px;")
        self.corrVal.setMaximum(100)
        self.corrVal.setOrientation(Qt.Horizontal)
        self.corrVal.setInvertedAppearance(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.corrVal)

        self.label_3 = QLabel(self.networkControls)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMargin(12)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.networkDates = QCheckBox(self.networkControls)
        self.networkDates.setObjectName(u"networkDates")
        self.networkDates.setStyleSheet(u"margin-top:18px")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.networkDates)

        self.label_4 = QLabel(self.networkControls)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMargin(12)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.networkColumn = QComboBox(self.networkControls)
        self.networkColumn.setObjectName(u"networkColumn")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.networkColumn)

        self.label_6 = QLabel(self.networkControls)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMargin(12)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.networkColNum = QSpinBox(self.networkControls)
        self.networkColNum.setObjectName(u"networkColNum")
        self.networkColNum.setMinimum(1)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.networkColNum)

        self.label_7 = QLabel(self.networkControls)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMargin(30)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.networkPlotbtn = QPushButton(self.networkControls)
        self.networkPlotbtn.setObjectName(u"networkPlotbtn")
        sizePolicy1.setHeightForWidth(self.networkPlotbtn.sizePolicy().hasHeightForWidth())
        self.networkPlotbtn.setSizePolicy(sizePolicy1)
        self.networkPlotbtn.setStyleSheet(u"margin-top:20px; margin-right:15px;")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.networkPlotbtn)

        self.networkToolBox.addItem(self.networkControls, u"Controls")
        self.networkTools = QWidget()
        self.networkTools.setObjectName(u"networkTools")
        self.networkTools.setGeometry(QRect(0, 0, 141, 56))
        self.verticalLayout_2 = QVBoxLayout(self.networkTools)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.networkexportbtn = QPushButton(self.networkTools)
        self.networkexportbtn.setObjectName(u"networkexportbtn")

        self.verticalLayout_2.addWidget(self.networkexportbtn)

        self.networkToolBox.addItem(self.networkTools, u"Tools")

        self.horizontalLayout_2.addWidget(self.networkToolBox)

        self.tabWidget.addTab(self.network, "")
        self.linegraph = QWidget()
        self.linegraph.setObjectName(u"linegraph")
        self.linegraph.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.linegraph)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.linegraphgridLayout = QGridLayout()
        self.linegraphgridLayout.setObjectName(u"linegraphgridLayout")
        self.linegraphgridLayout.setSizeConstraint(QLayout.SetMaximumSize)

        self.horizontalLayout_3.addLayout(self.linegraphgridLayout)

        self.linetoolBox = QToolBox(self.linegraph)
        self.linetoolBox.setObjectName(u"linetoolBox")
        self.linetoolBox.setMaximumSize(QSize(350, 16777215))
        self.linetoolBox.setStyleSheet(u"background-color: rgb(27, 30, 43);")
        self.linegraphControls = QWidget()
        self.linegraphControls.setObjectName(u"linegraphControls")
        self.linegraphControls.setGeometry(QRect(0, 0, 350, 617))
        self.linegraphControls.setMaximumSize(QSize(16777215, 16777215))
        self.formLayout_3 = QFormLayout(self.linegraphControls)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(24, -1, 24, -1)
        self.label_9 = QLabel(self.linegraphControls)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setMargin(12)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.lineCity = QComboBox(self.linegraphControls)
        self.lineCity.setObjectName(u"lineCity")
        self.lineCity.setStyleSheet(u"")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineCity)

        self.label_10 = QLabel(self.linegraphControls)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMargin(12)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.lineXCol = QComboBox(self.linegraphControls)
        self.lineXCol.setObjectName(u"lineXCol")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineXCol)

        self.label_11 = QLabel(self.linegraphControls)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setMargin(12)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.lineYCol = QComboBox(self.linegraphControls)
        self.lineYCol.setObjectName(u"lineYCol")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineYCol)

        self.label_12 = QLabel(self.linegraphControls)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setMargin(12)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_12)

        self.linePlotbtn = QPushButton(self.linegraphControls)
        self.linePlotbtn.setObjectName(u"linePlotbtn")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.linePlotbtn)

        self.linetoolBox.addItem(self.linegraphControls, u"Controls")
        self.linegraphTools = QWidget()
        self.linegraphTools.setObjectName(u"linegraphTools")
        self.linegraphTools.setGeometry(QRect(0, 0, 149, 56))
        self.verticalLayout_3 = QVBoxLayout(self.linegraphTools)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(24, -1, 24, -1)
        self.linegraphExport = QPushButton(self.linegraphTools)
        self.linegraphExport.setObjectName(u"linegraphExport")

        self.verticalLayout_3.addWidget(self.linegraphExport)

        self.linetoolBox.addItem(self.linegraphTools, u"Tools")

        self.horizontalLayout_3.addWidget(self.linetoolBox)

        self.tabWidget.addTab(self.linegraph, "")
        self.scatter = QWidget()
        self.scatter.setObjectName(u"scatter")
        self.horizontalLayout_4 = QHBoxLayout(self.scatter)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scattergridLayout = QGridLayout()
        self.scattergridLayout.setObjectName(u"scattergridLayout")

        self.horizontalLayout_4.addLayout(self.scattergridLayout)

        self.scattertoolBox = QToolBox(self.scatter)
        self.scattertoolBox.setObjectName(u"scattertoolBox")
        self.scattertoolBox.setMaximumSize(QSize(350, 16777215))
        self.scattertoolBox.setStyleSheet(u"background-color: rgb(27, 30, 43);")
        self.scatterControls = QWidget()
        self.scatterControls.setObjectName(u"scatterControls")
        self.scatterControls.setGeometry(QRect(0, 0, 350, 617))
        self.formLayout_4 = QFormLayout(self.scatterControls)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(24, -1, 24, -1)
        self.label_13 = QLabel(self.scatterControls)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMargin(12)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.scatterCity = QComboBox(self.scatterControls)
        self.scatterCity.setObjectName(u"scatterCity")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.scatterCity)

        self.label_14 = QLabel(self.scatterControls)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMargin(12)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.scatterXCol = QComboBox(self.scatterControls)
        self.scatterXCol.setObjectName(u"scatterXCol")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.scatterXCol)

        self.label_15 = QLabel(self.scatterControls)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMargin(12)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.scatterYCol = QComboBox(self.scatterControls)
        self.scatterYCol.setObjectName(u"scatterYCol")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.scatterYCol)

        self.label_16 = QLabel(self.scatterControls)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMargin(12)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_16)

        self.scatterPlotbtn = QPushButton(self.scatterControls)
        self.scatterPlotbtn.setObjectName(u"scatterPlotbtn")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.scatterPlotbtn)

        self.scattertoolBox.addItem(self.scatterControls, u"Controls")
        self.scatterTools = QWidget()
        self.scatterTools.setObjectName(u"scatterTools")
        self.scatterTools.setGeometry(QRect(0, 0, 134, 71))
        self.horizontalLayout_5 = QHBoxLayout(self.scatterTools)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(24, -1, -1, 24)
        self.scatterExportbtn = QPushButton(self.scatterTools)
        self.scatterExportbtn.setObjectName(u"scatterExportbtn")

        self.horizontalLayout_5.addWidget(self.scatterExportbtn)

        self.scattertoolBox.addItem(self.scatterTools, u"Tools")

        self.horizontalLayout_4.addWidget(self.scattertoolBox)

        self.tabWidget.addTab(self.scatter, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 35))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menufile.addAction(self.actionOpen_File)
        self.menufile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionShow_Startup_Dialog)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.choroplothtoolBox.setCurrentIndex(0)
        self.networkToolBox.setCurrentIndex(0)
        self.networkToolBox.layout().setSpacing(12)
        self.linetoolBox.setCurrentIndex(0)
        self.scattertoolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(statustip)
        self.actionExit.setStatusTip(QCoreApplication.translate("MainWindow", u"Exit (Ctrl+Q)", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.actionExit.setWhatsThis(QCoreApplication.translate("MainWindow", u"Exit the Application", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(tooltip)
        self.actionAbout.setToolTip(QCoreApplication.translate("MainWindow", u"For now exits the Application", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionAbout.setStatusTip(QCoreApplication.translate("MainWindow", u"For now exits the Application", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.actionAbout.setWhatsThis(QCoreApplication.translate("MainWindow", u"For now exits the Application", None))
#endif // QT_CONFIG(whatsthis)
        self.actionShow_Startup_Dialog.setText(QCoreApplication.translate("MainWindow", u"Show Startup Dialog", None))
#if QT_CONFIG(statustip)
        self.actionShow_Startup_Dialog.setStatusTip(QCoreApplication.translate("MainWindow", u"Show Startup Dialog", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.actionShow_Startup_Dialog.setWhatsThis(QCoreApplication.translate("MainWindow", u"Show Startup Dialog", None))
#endif // QT_CONFIG(whatsthis)
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionOpen_File.setIconText(QCoreApplication.translate("MainWindow", u"Open File", None))
#if QT_CONFIG(statustip)
        self.actionOpen_File.setStatusTip(QCoreApplication.translate("MainWindow", u"Open File (Ctrl+O)", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.actionOpen_File.setWhatsThis(QCoreApplication.translate("MainWindow", u"Open File", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(shortcut)
        self.actionOpen_File.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Network Plot </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tabWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(statustip)
        self.choropleth.setStatusTip(QCoreApplication.translate("MainWindow", u"ChoroPleth Plot", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.choropleth.setWhatsThis(QCoreApplication.translate("MainWindow", u"ChoroPleth Plot", None))
#endif // QT_CONFIG(whatsthis)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Column", None))
        self.choroColumn.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Column", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.choroPlotbtn.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.choroplothtoolBox.setItemText(self.choroplothtoolBox.indexOf(self.choroControls), QCoreApplication.translate("MainWindow", u"Controls", None))
        self.choroexportbtn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.choroplothtoolBox.setItemText(self.choroplothtoolBox.indexOf(self.choroTools), QCoreApplication.translate("MainWindow", u"Tools", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.choropleth), QCoreApplication.translate("MainWindow", u"ChoroPleth", None))
#if QT_CONFIG(statustip)
        self.network.setStatusTip(QCoreApplication.translate("MainWindow", u"Network Plot", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.network.setWhatsThis(QCoreApplication.translate("MainWindow", u"Network Plot", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Correlation Direction", None))
        self.corrDir.setItemText(0, QCoreApplication.translate("MainWindow", u"positive", None))
        self.corrDir.setItemText(1, QCoreApplication.translate("MainWindow", u"negative", None))

        self.corrDir.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Correlation", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Correlation Value", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"With Dates", None))
        self.networkDates.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Column", None))
        self.networkColumn.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Column", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Number of Rows", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.networkPlotbtn.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.networkToolBox.setItemText(self.networkToolBox.indexOf(self.networkControls), QCoreApplication.translate("MainWindow", u"Controls", None))
        self.networkexportbtn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.networkToolBox.setItemText(self.networkToolBox.indexOf(self.networkTools), QCoreApplication.translate("MainWindow", u"Tools", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.network), QCoreApplication.translate("MainWindow", u"Network", None))
#if QT_CONFIG(whatsthis)
        self.tabWidget.setTabWhatsThis(self.tabWidget.indexOf(self.network), QCoreApplication.translate("MainWindow", u"Network Plot", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(statustip)
        self.linegraph.setStatusTip(QCoreApplication.translate("MainWindow", u"LineGraph", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.linegraph.setWhatsThis(QCoreApplication.translate("MainWindow", u"LineGraph", None))
#endif // QT_CONFIG(whatsthis)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"City", None))
        self.lineCity.setPlaceholderText(QCoreApplication.translate("MainWindow", u"select City", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"x-axis", None))
        self.lineXCol.setPlaceholderText(QCoreApplication.translate("MainWindow", u"select column", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"y-axis", None))
        self.lineYCol.setPlaceholderText(QCoreApplication.translate("MainWindow", u"select column", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.linePlotbtn.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.linetoolBox.setItemText(self.linetoolBox.indexOf(self.linegraphControls), QCoreApplication.translate("MainWindow", u"Controls", None))
        self.linegraphExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.linetoolBox.setItemText(self.linetoolBox.indexOf(self.linegraphTools), QCoreApplication.translate("MainWindow", u"Tools", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.linegraph), QCoreApplication.translate("MainWindow", u"Line Graph", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.linegraph), QCoreApplication.translate("MainWindow", u"Hotspot Plot", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tabWidget.setTabWhatsThis(self.tabWidget.indexOf(self.linegraph), QCoreApplication.translate("MainWindow", u"Hotspot Plot", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(statustip)
        self.scatter.setStatusTip(QCoreApplication.translate("MainWindow", u"ScatterPlot", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.scatter.setWhatsThis(QCoreApplication.translate("MainWindow", u"ScatterPlot", None))
#endif // QT_CONFIG(whatsthis)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"City", None))
        self.scatterCity.setPlaceholderText(QCoreApplication.translate("MainWindow", u"select City", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"x-axis", None))
        self.scatterXCol.setPlaceholderText(QCoreApplication.translate("MainWindow", u"select column", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"y-axis", None))
        self.scatterYCol.setPlaceholderText(QCoreApplication.translate("MainWindow", u"select column", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.scatterPlotbtn.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.scattertoolBox.setItemText(self.scattertoolBox.indexOf(self.scatterControls), QCoreApplication.translate("MainWindow", u"Controls", None))
        self.scatterExportbtn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.scattertoolBox.setItemText(self.scattertoolBox.indexOf(self.scatterTools), QCoreApplication.translate("MainWindow", u"Tools", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scatter), QCoreApplication.translate("MainWindow", u"Scatter Plot", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


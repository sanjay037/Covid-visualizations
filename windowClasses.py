# This Python file uses the following encoding: utf-8
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QUrl, QSettings, QCoreApplication
from PySide2.QtWidgets import (
    QApplication, QFileDialog,
    QMainWindow,
    QGraphicsDropShadowEffect,
    QStyle,
    QDialog,
    QGridLayout
)
from PySide2.QtGui import QColor, QIcon, QFont, QGuiApplication
import networkx
from ui_splash import Ui_splashScreen
from ui_main import Ui_MainWindow
from ui_startupDialog import Ui_welcomeDialog
from ui_about import Ui_AboutDialog
from matwin import MatWin
from plotlywin import PlotlyWin
from linewin import LineWin
from scatterwin import ScatterWin

counter = 0
fileName = ""

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Visualization Tool")
        self.move(QGuiApplication.primaryScreen().availableGeometry().center()- self.rect().center())

        # Network Viz
        self.network = MatWin(self.ui.network)
        network_Cols,network_ColName,network_isDate,network_corrdir,network_corrVal,network_numCol = self.network.getValues()
        self.ui.networkColNum.setValue(network_numCol)
        self.ui.corrVal.setValue(network_corrVal*100)
        self.ui.corrDir.setCurrentIndex(0 if network_corrdir== "positive" else 1)
        self.ui.networkColumn.addItems(network_Cols)
        self.ui.networkColumn.setCurrentIndex(1)
        gridnetwork = self.ui.networkgridLayout
        gridnetwork.addWidget(self.network, 0, 0, 1, 1)
        self.ui.networkPlotbtn.clicked.connect(self.networkPlot)
        self.ui.networkexportbtn.clicked.connect(lambda: self.saveFigure("Network"))

        # Choropleth Viz
        self.choropleth = PlotlyWin(self.ui.choropleth)
        choroValues = self.choropleth.get_columns()
        self.ui.choroColumn.addItems(choroValues)
        chorogridnetwork = self.ui.choroplethgridLayout
        chorogridnetwork.addWidget(self.choropleth, 0, 0, 1, 1)
        self.ui.choroPlotbtn.clicked.connect(self.choroPlot)
        self.ui.choroexportbtn.setEnabled(False)

        #line graph
        self.linegraph = LineWin(self.ui.linegraph)
        self.ui.linegraphgridLayout.addWidget(self.linegraph,0,0,1,1)
        lineCols,lineX,lineY,lineCityNames,lineCityid = self.linegraph.getValues()
        self.ui.lineCity.addItems(lineCityNames)
        self.ui.lineCity.setCurrentIndex(lineCityid-1)
        self.ui.lineXCol.addItems(lineCols)
        self.ui.lineXCol.setCurrentText(lineX)
        self.ui.lineYCol.addItems(lineCols)
        self.ui.lineYCol.setCurrentText(lineY)
        self.ui.linePlotbtn.clicked.connect(self.linePlot)
        self.ui.linegraphExport.clicked.connect(lambda: self.saveFigure("LineGraph"))

        #Scatter Plot
        self.scatter = ScatterWin(self.ui.scatter)
        self.ui.scattergridLayout.addWidget(self.scatter,0,0,1,1)
        scatterCols,scatterX,scatterY,scatterCityNames,scatterCityid = self.scatter.getValues()
        self.ui.scatterCity.addItems(scatterCityNames)
        self.ui.scatterCity.setCurrentIndex(scatterCityid-1)
        self.ui.scatterXCol.addItems(scatterCols)
        self.ui.scatterXCol.setCurrentText(scatterX)
        self.ui.scatterYCol.addItems(scatterCols)
        self.ui.scatterYCol.setCurrentText(scatterY)
        self.ui.scatterPlotbtn.clicked.connect(self.scatterPlot)
        self.ui.scatterExportbtn.clicked.connect(lambda: self.saveFigure("Scatter"))

        self.ui.actionOpen_File.triggered.connect(self.openfile)
        self.ui.actionExit.triggered.connect(self.exitApp)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionShow_Startup_Dialog.triggered.connect(self.openStartDialog)

        self.diag = StartUpDialog()
        # self.ui.horizontalLayout_2.setLayout(gridnetwork)

    def choroPlot(self):
        self.choropleth.setvalue(self.ui.choroColumn.currentText())
        print(self.ui.choroColumn.currentText())
        self.choropleth.show_graph()

    def networkPlot(self):
        self.network.setValues(fileName,self.ui.networkColumn.currentText(),self.ui.networkDates.isChecked(),self.ui.corrDir.currentText(),self.ui.corrVal.value(),self.ui.networkColNum.text())
        self.network.plot()

    def linePlot(self):
        self.linegraph.setValues(fileName,self.ui.lineXCol.currentText(),self.ui.lineYCol.currentText(),self.ui.lineCity.currentIndex())
        self.linegraph.plot()

    def scatterPlot(self):
        self.scatter.setValues(fileName,self.ui.scatterXCol.currentText(),self.ui.scatterYCol.currentText(),self.ui.scatterCity.currentIndex())
        self.scatter.plot()

    def openfile(self):
        global fileName
        filename,_= QFileDialog.getOpenFileName(self, self.tr("Load DataFile"), self.tr("~/Documents/"), self.tr("CSV files (*.csv)"))
    
    def saveFigure(self,winType):
        fileDialog = QFileDialog(self)
        fileDialog.setAcceptMode( QFileDialog.AcceptSave)
        fileName,_ = fileDialog.getSaveFileName(self, self.tr("Save File"),
                                       "~/untitled.png",
                                       self.tr("Images (*.png *.xpm *.jpg)"))
        if winType== "Network":
            figure=self.network.figure
        elif winType=="LineGraph":
            figure=self.linegraph.figure
        elif winType=="Scatter":
            figure=self.scatter.figure
        else:
            figure=self.network.figure
        figure.savefig(fileName, dpi=figure.dpi, transparent=True)

    def about(self):
        self.about = AboutDialog()
        self.about.show()

    def openStartDialog(self):
        self.diag.show()

    def writeSettings(self):
        pass

    def exitApp(self):
        self.close()

    # event : QCloseEvent
    def closeEvent(self, event):
        self.writeSettings()
        if(self.diag.isVisible()):
            self.diag.close()
        event.accept()

class AboutDialog(QDialog):

    def __init__(self):
         QDialog.__init__(self)
         self.ui = Ui_AboutDialog()
         self.ui.setupUi(self)
         self.setWindowTitle("About")

class StartUpDialog(QDialog):
    recentFiles=[]
    sampleFiles = ["Affinity-City-Daily.csv"]

    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_welcomeDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Welcome")
        self.ui.newfilebtn.clicked.connect(self.getFilename)
        if (self.recentFiles != []):
            self.ui.openRecentList.setViewMode(QtWidgets.QListView.IconMode)
            self.recentmodel = QtGui.QStandardItemModel()
            self.ui.openRecentList.setModel(self.recentmodel)
            for i in self.recentFiles:
                item = QtGui.QStandardItem(i)
                self.recentmodel.appendRow(item)
                item.setIcon(QtWidgets.QFileIconProvider().icon(QtWidgets.QFileIconProvider.File))
        else:
            self.ui.gridLayout.removeWidget(self.ui.openRecentList)
            font1 = QFont()
            font1.setFamily(u"Segoe UI")
            font1.setPointSize(12)
            self.recentLabel = QtWidgets.QLabel("No Recent files")
            self.recentLabel.setText("No Recent files")
            self.recentLabel.setFont(font1)
            self.recentLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.recentLabel.setStyleSheet(u"margin-left:20px;")
            self.ui.gridLayout.addWidget(self.recentLabel, 5, 0, 4, 1)
        self.ui.samplesList.setViewMode(QtWidgets.QListView.IconMode)
        self.sampleModel = QtGui.QStandardItemModel()
        self.ui.samplesList.setModel(self.sampleModel)
        for i in self.sampleFiles:
                item = QtGui.QStandardItem(i)
                self.sampleModel.appendRow(item)
                item.setIcon(QtWidgets.QFileIconProvider().icon(QtWidgets.QFileIconProvider.File))
        self.ui.samplesList.clicked.connect(self.closeFunction)

    def getFilename(self):
        global fileName
        filename,_= QFileDialog.getOpenFileName(self, self.tr("Load DataFile"), self.tr("~/Documents/"), self.tr("CSV files (*.csv)"))
        self.close()

    def closeFunction(self):
        self.close()

    def writeSettings(self):
        settings = QSettings()
        settings.beginGroup("StartUpDialog")
        settings.setValue("openAtStartUp",self.ui.startupCheckbox.isChecked())

    # event : QCloseEvent
    def closeEvent(self, event):
        self.writeSettings()
        event.accept()


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_splashScreen()
        self.ui.setupUi(self)
        self.setWindowTitle("Splash Screen")
        self.move(QGuiApplication.primaryScreen().availableGeometry().center()- self.rect().center())
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(20)
        self.ui.label_status.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        QtCore.QTimer.singleShot(
            500,
            lambda: self.ui.label_status.setText(
                "<strong>LOADING</strong> DATABASE"
            ),
        )
        QtCore.QTimer.singleShot(
            1000,
            lambda: self.ui.label_status.setText(
                "<strong>LOADING</strong> USER INTERFACE"
            ),
        )
        self.show()
        self.main = MainWindow()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            # self.main.setGeometry(
            #     QStyle.alignedRect(
            #         QtCore.Qt.LeftToRight,
            #         QtCore.Qt.AlignCenter,
            #         window.size(),
            #         QGuiApplication.primaryScreen().availableGeometry(),
            #     ),
            # )
            self.main.show()
            self.close()
            self.main.diag.show()
            self.main.diag.exec_()

        counter += 1


if __name__ == "__main__":
    app = QApplication([])
    QCoreApplication.setOrganizationName("kingavatar")
    # QCoreApplication.setOrganizationDomain("")
    QCoreApplication.setApplicationName("Covid Dashboard")
    window = SplashScreen()
    # window.setGeometry(
    #     QStyle.alignedRect(
    #         QtCore.Qt.LeftToRight,
    #         QtCore.Qt.AlignCenter,
    #         window.size(),
    #         QGuiApplication.primaryScreen().availableGeometry(),
    #     ),
    # )
    sys.exit(app.exec_())

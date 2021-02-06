import sys
from PySide2.QtWidgets import QFileDialog, QWidget, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# matplotlib widget
# which inherits QDialog
class ScatterWin(QWidget):
    filename = "Affinity-City-Daily.csv"
    columnName = "spend_all"
    columnName2 = "date"
    cityid=1
    # constructor
    def __init__(self, parent=None):
        super(ScatterWin, self).__init__(parent)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        citydata = pd.read_csv('GeoIDs-City.csv')
        self.citynames = list(citydata['cityname'])
        self.ax = self.figure.add_subplot(111)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to 'plot' method
        # self.button = QPushButton("Plot")

        # adding action to the button
        # self.button.clicked.connect(self.plot)

        # creating a Vertical Box layout
        layout = QVBoxLayout()

        # adding tool bar to the layout
        layout.addWidget(self.toolbar)

        # adding canvas to the layout
        layout.addWidget(self.canvas)

        # adding push button to the layout
        # layout.addWidget(self.button)

        # setting layout to the main window
        self.setLayout(layout)
        self.plot()
        self.plot()


    # action called by the push button
    def plot(self):

        # self.figure.clear()
        self.ax.clear()
        # self.ax.set_axis_off()
        df = pd.read_csv(self.filename)
        df = df.replace('.',np.nan)
        df = df.dropna()
        date = pd.to_datetime(df[['day', 'month','year']])
        df = df.drop(['year','month','day','freq'],axis=1)
        df.insert(0,column='date',value=date)
        self.columns = df.columns
        self.columns=list(self.columns)
        if 'cityid' in self.columns:
            self.columns.remove('cityid')
        self.ax.scatter(df.loc[df['cityid']==self.cityid][self.columnName2],df.loc[df['cityid']==self.cityid][self.columnName],s=10)
        self.ax.spines["top"].set_color("None") 
        self.ax.spines["right"].set_color("None")
        self.ax.set(xlabel=self.columnName2,ylabel=self.columnName,title="Scatter Plot of "+self.columnName+" vs "+self.columnName2+" of city "+self.citynames[self.cityid-1])

        # refresh canvas
        self.canvas.draw()

    def setValues(self, filename, columnName2,columnName,cityid):
        # print(filename, columnName, isDate, corrDir, corrVal / 100.00, numCol)
        if filename != "":
            self.filename = filename
        self.columnName = columnName
        if self.columnName2!="":
            self.columnName2 = columnName2
        self.cityid = int(cityid)+1

    def getValues(self):
        return (
            self.columns,
            self.columnName2,
            self.columnName,
            self.citynames,
            self.cityid
        )



# driver code
if __name__ == "__main__":

    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = ScatterWin()

    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())

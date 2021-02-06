import sys
from PySide2.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from node_link import node_link


# matplotlib widget
# which inherits QDialog
class MatWin(QWidget):
    filename = "Affinity-City-Daily.csv"
    columnName = "spend_aer"
    isDate = False
    corrDir = "positive"
    corrVal = 0.95
    numCol = 50

    # constructor
    def __init__(self, parent=None):
        super(MatWin, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()
        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        # self.columns = node_link(
        #     "Affinity-City-Daily.csv",
        #     self.figure,
        #     "spend_aer",
        #     False,
        #     "positive",
        #     0.95,
        #     50,
        # )
        self.ax = self.figure.add_subplot(111)

        self.columns = node_link(
            self.filename,
            self.ax,
            self.columnName,
            self.isDate,
            self.corrDir,
            self.corrVal,
            self.numCol,
        )
        # this is the Navigation widget
        # it takes the Canvas widget and a parent
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

    # action called by the push button
    def plot(self):

        # random data
        # data = [random.random() for i in range(10)]

        # clearing old figure
        # self.figure.clear()
        self.ax.clear()
        self.ax.set_axis_off()
        # create an axis
        # ax = self.figure.add_subplot(111)

        # plot data
        # ax.plot(data, '*-')
        # node_link(
        #     "Affinity-City-Daily.csv",
        #     self.figure,
        #     "spend_aer",
        #     False,
        #     "positive",
        #     0.95,
        #     50,
        # )
        node_link(
            self.filename,
            self.ax,
            self.columnName,
            self.isDate,
            self.corrDir,
            self.corrVal,
            self.numCol,
        )
        # refresh canvas
        self.canvas.draw()

    def setValues(self, filename:str, columnName:str, isDate:bool, corrDir:str, corrVal:float, numCol:str or int):
        # print(filename, columnName, isDate, corrDir, corrVal / 100.00, numCol)
        if filename != "":
            self.filename = filename
        self.columnName = columnName
        self.isDate = isDate
        self.corrDir = corrDir
        self.corrVal = corrVal / 100.00
        self.numCol = int(numCol)

    def getValues(self):
        return (
            self.columns,
            self.columnName,
            self.isDate,
            self.corrDir,
            self.corrVal,
            self.numCol,
        )


# driver code
if __name__ == "__main__":

    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = MatWin()

    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())

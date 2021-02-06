from PySide2 import QtCore, QtWidgets, QtWebEngineWidgets
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from choropleth import get_slider, preprocess_education

class PlotlyWin(QtWidgets.QWidget):
    attribute_name = 'Numerical_status'
    small_name_attribute = 'Status'
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.button = QtWidgets.QPushButton('Plot', self)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        data = pd.read_csv('covid_impact_education.csv')
        self.data = preprocess_education(data)
        vlayout = QtWidgets.QVBoxLayout(self)
        # vlayout.addWidget(self.button, alignment=QtCore.Qt.AlignHCenter)
        vlayout.addWidget(self.browser)
        self.show_graph()
        # self.button.clicked.connect(self.show_graph)
        self.resize(1000,800)

    def show_graph(self):
        units = ''
        start_date = '16/02/2020'
        end_date = '16/12/2020'
        fig_data = get_slider(self.data, self.attribute_name, self.small_name_attribute, units, start_date, end_date)
        fig=go.Figure(fig_data)
        # plotly.offline.iplot(fig)
        # df = px.data.tips()
        # fig = px.box(df, x="day", y="total_bill", color="smoker")
        # fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def get_columns(self):
        col = list(self.data.columns)
        if 'Date' in col:
            col.remove('Date')
        if 'ISO' in col:
            col.remove('ISO')
        if 'Country' in col:
            col.remove('Country')
        if 'Note' in col:
            col.remove('Note')
        if 'Status' in col:
            col.remove('Status')
        return col
    
    def setvalue(self,columnname):
        self.attribute = columnname
        self.attribute_name = columnname


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = PlotlyWin()
    widget.show()
    app.exec_()

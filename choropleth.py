import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns
# %matplotlib inline
import country_converter as coco
import plotly.express as px
import plotly
import plotly.graph_objs as go
import plotly.offline as offline
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


def preprocess_education(data):
	  l = []
	  mapping_dict = {'Fully open':10,'Partially open':5,'Academic break':0, 'Closed due to COVID-19':-10}
	  for index, row in data.iterrows():
	    l.append(mapping_dict[row['Status']])
	  data['Numerical_status'] = l
	  return data

def get_slider(data, attribute, attr_display_name, units, start_date, end_date):
	  data_slider = []

	  for date in data['Date'].unique():
	    if date > end_date or date < start_date:
	      continue
	    for col in data[data['Date'] == date].columns:
	      data.loc[data['Date'] == date,col] = list(data.loc[data['Date'] == date,col].astype(str))
	    df_date = data[data['Date'] == date]

	    data_date = dict(
	        type='choropleth',
	        locations = df_date['ISO'],
	        z = df_date[attribute],
	        text = df_date['Country'],
	        colorscale = 'rdylgn',
	        autocolorscale=False,
	        reversescale=False,
	        marker_line_color='darkgray',
	        marker_line_width=0.5,
	        colorbar_tickprefix = units,
	        colorbar_title = attr_display_name+"<br>"+units
	    )
	    data_slider.append(data_date)
	  steps = []
	  dates = list(data['Date'].unique())
	  dates.sort()
	  for i in range(len(data_slider)):
	      step = dict(method='restyle',
	                  args=['visible', [False] * len(data_slider)],
	                  label=dates[i]) # label to be displayed for each step (year)
	      step['args'][1][i] = True
	      steps.append(step)


	  sliders = [dict(active=0, pad={"t": 1}, steps=steps)]
	  layout = dict(
	      title_text="Global changes in "+attr_display_name+" over time",
	      geo=dict(
	          showframe=True,
	          showcoastlines=True,
	          projection_type='equirectangular'
	      ),
	      annotations = [dict(
	          x=0.55,
	          y=0.1,
	          xref='paper',
	          yref='paper',
	          text='Source: <a href="https://data.world/liz-friedman/covid-19-impact-on-education">\
	              COVID 19 Impact on Education</a>',
	          showarrow = False
	      )],
	      sliders = sliders)
	  fig = dict(data=data_slider, layout=layout)
	  return fig
	# data = pd.read_csv('file')
	# data1 = preprocess_education(data)
	# attribute_name = 'Numerical_status'
	# small_name_attribute = 'Status'
	# units = ''
	# start_date = '16/02/2020'
	# end_date = '16/12/2020'
	# fig = get_slider(data1, attribute_name, small_name_attribute, units, start_date, end_date)
	# plotly.offline.iplot(fig)

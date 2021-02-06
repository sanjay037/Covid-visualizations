# just call the function node_link

import numpy as np
import pandas as pd
from math import sqrt
import networkx as nx
import matplotlib.pyplot as plt

def create_corr_network_4(G,ax, corr_direction, min_corr_value,between_dates,column_name):
    H = G.copy()
    #Checks all the edges and removes some based on corr_direction
    for stock1, stock2, weight in G.edges(data=True):
        #if we only want to see the positive correlations we then delete the edges with weight smaller than 0        
        if corr_direction == "positive":
            if weight["weight"] <0 or weight["weight"] < min_corr_value:
                H.remove_edge(stock1, stock2)
        #this part runs if the corr_direction is negative and removes edges with weights equal or largen than 0
        else:
            if weight["weight"] >=0 or weight["weight"] > min_corr_value:
                H.remove_edge(stock1, stock2)
                
    
    #crates a list for edges and for the weights
    edges,weights = zip(*nx.get_edge_attributes(H,'weight').items())
    
    #increases the value of weights, so that they are more visible in the graph
    weights = tuple([(1+abs(x))**2 for x in weights])

    #positions
    positions=nx.random_layout(H)
    
    #Figure size
    #figsize=(15,15)
    # plt.figure()
    # fig.add_subplot(111)
    #draws nodes
    nx.draw_networkx_nodes(H,positions,node_color='#DA70D6',node_size=500,alpha=0.8,ax=ax)
    
    #Styling for labels
    nx.draw_networkx_labels(H, positions, font_size=8,font_family='sans-serif',ax=ax)
    
    #edge colors based on weight direction
    if corr_direction == "positive":
        edge_colour = plt.cm.GnBu 
    else:
        edge_colour = plt.cm.PuRd
        
    #draws the edges
    nx.draw_networkx_edges(H, positions,edgelist=edges,style='solid',width=weights, 
                            edge_color = weights, edge_cmap = edge_colour,edge_vmin = min(weights), 
                            edge_vmax=max(weights),ax=ax)

    # displays the graph without axis
    plt.axis('off')
    if between_dates:
        ax.set_title(corr_direction+" correlation of "+ column_name +" between dates")
    else:
        ax.set_title(corr_direction+" correlation of "+ column_name +" between countries")
    # plt.show() 


def node_link(file_name,ax,column_name,between_dates,corr_dir,min_corr_value,n):
    df = pd.read_csv(file_name)
    # drop null values
    df = df.replace('.',np.nan)
    df = df.dropna()
    # change day month and year columns to date column
    date = pd.to_datetime(df[['day', 'month','year']])
    df = df.drop(['year','month','day','freq'],axis=1)
    df.insert(0,column='date',value=date)
    # store all dates and city id's and drop columns
    date = np.unique(df["date"].dt.strftime('%m-%d-%y'))
    df = df.drop(['date'],axis=1)
    city = np.unique(df['cityid'])
    df = df.drop(['cityid'],axis=1) 
    # create new dataframe with cities as columns and dates as rows
    c = pd.read_csv('GeoIDs-City.csv') 
    city_names = []
    city_abb = []
    for i in range(len(c['cityid'])):
        city_names.append(c.iloc[i]['cityname'])
        city_abb.append(c.iloc[i]['stateabbrev'])
    temp_count = 0
    for i in range(len(city)):
        if(city[i]!=(temp_count+1)):
            city_names.pop(temp_count)
            temp_count +=1
        temp_count+=1
    k=0
    l = []
    for j in range(len(date)):
        temp = []
        for i in range(len(city)):
            temp.append(df.iloc[k][column_name])
            k+=1
        l.append(temp)
    data = pd.DataFrame(l, columns = ["%d" % (i + 1) for i in range(len(city))])
    # for plotting between dates
    if between_dates:
        data = data.iloc[0:n]
        data = data.T
    else:
        data = data.T
        data = data.iloc[0:n]
        data = data.T
    # compute correlation matrix
    cor_matrix= data.astype('float64').corr()
    cor_matrix = np.asmatrix(cor_matrix)
    # create graph
    G = nx.from_numpy_matrix(cor_matrix)
    if between_dates:
        G = nx.relabel_nodes(G,lambda x: date[x])
    else:   
        G = nx.relabel_nodes(G,lambda x: city_names[x])
    create_corr_network_4(G,ax, corr_dir, min_corr_value, between_dates,column_name)
    return df.columns


# inputs: file name, column name, False for between country and true for between dates, 
# direction(positive or negative), min coorelation, to select n dates or countries)
# node_link('Affinity-City-Daily.csv','spend_aer',True,'positive',0.9,50)
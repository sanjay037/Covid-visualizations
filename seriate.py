import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
import plotly.graph_objects as go
from scipy.spatial.distance import pdist
from seriate import seriate

def seriate_on(cor_matrix, bool_seriate):
    if bool_seriate:
        cols = seriate(pdist(cor_matrix))
        cor_matrix[:] = [cor_matrix[i] for i in cols]
        G = nx.from_numpy_matrix(cor_matrix)
        plt.clf()
        heatmap = sns.heatmap(cor_matrix, )
        return cor_matrix, heatmap
    else:
        heatmap = sns.heatmap(cor_matrix, )
        return cor_matrix, heatmap

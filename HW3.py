import pandas as pd
import numpy as np
import networkx as nx
from networkx.algorithms.bipartite import sets, weighted_projected_graph
import matplotlib.pyplot as plt


# Read in the data
matrix = pd.read_csv("userRatedMovie.csv")

# Create Bipartite Graph from Pandas dataframe
bg = nx.from_pandas_edgelist(matrix, source="name", target="title", edge_attr="userRating")

# Distinguish difference between movie node and critic node by making two sets (l set and r set)
l, r = nx.bipartite.sets(bg)	#l is critics, r is movies

# Assign position for each node (how it gets rendered with matplotlib)
pos = {}
pos.update((node, (0,index)) for index, node in enumerate(l)) #Critics
pos.update((node, (1,index)) for index, node in enumerate(r)) #Movies

# Change color of node based on whether its a critic or movie
color_map = []
for node in bg:
	if node in l:
		color_map.append("red")
	else:
		color_map.append("blue")

nx.draw(bg, pos=pos, node_color=color_map, with_labels=True)
plt.show()

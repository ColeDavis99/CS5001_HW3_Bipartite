import pandas as pd
import numpy as np
import networkx as nx
from networkx.algorithms.bipartite import sets, weighted_projected_graph
import matplotlib.pyplot as plt


# Function that prints the key with the largest numeric value in a dict
def DictLargestValue(dictionary, critic_list, centrality_type):
	topMovieKey = ""
	largestMovieVal = -1
	
	topCriticKey = ""
	largestCriticVal = -1
	
	
	for key in dictionary.keys():
		if(key in critic_list):				#This if statement takes care of the critics
			if(dictionary[key] > largestCriticVal):
				largestCriticVal = dictionary[key]
				topCriticKey = key
		else:							#This else statement takes care of the movies
			if(dictionary[key] > largestMovieVal):
				largestMovieVal = dictionary[key]
				topMovieKey = key
				
		#print(dictionary[key], key)
				
	print("Top critic for", centrality_type, "centrality is:", topCriticKey, "with score of", largestCriticVal)
	print("Top movie for", centrality_type, "centrality is:", topMovieKey, "with score of", largestMovieVal)
	print()
		



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


# List the most important movie and most important critic for the following centrality metrics: degree, closeness, betweenness
# Second argument could be l or r, score for all nodes are returned regardless
dc = nx.bipartite.degree_centrality(bg, l)
cc = nx.bipartite.closeness_centrality(bg, l)
bc = nx.bipartite.betweenness_centrality(bg, l)

DictLargestValue(dc, list(l), "degree")
DictLargestValue(cc, list(l), "closeness")
DictLargestValue(bc, list(l), "betweenness")


# Apply color and position changes, then display with matplotlib
nx.draw(bg, pos=pos, node_color=color_map, with_labels=True)
#plt.show()

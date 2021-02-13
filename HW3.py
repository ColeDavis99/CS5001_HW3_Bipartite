import pandas as pd
import numpy as np
import networkx as nx
from networkx.algorithms.bipartite import sets, weighted_projected_graph
import matplotlib.pyplot as plt


# Read in the data
matrix = pd.read_csv("userRatedMovie.csv")

# Create Bipartite Graph from Pandas dataframe
bg = nx.from_pandas_edgelist(matrix, source="name", target="title", edge_attr="userRating")



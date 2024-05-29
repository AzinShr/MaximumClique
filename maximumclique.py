# -*- coding: utf-8 -*-

import networkx as nx
import dwave_networkx as dnx
from dwave.system import DWaveSampler, EmbeddingComposite

# Create a random graph
num_nodes = 10  # Number of nodes
edge_prob = 0.5  # Probability of edge creation

G = nx.erdos_renyi_graph(num_nodes, edge_prob)

# Set up the sampler
sampler = EmbeddingComposite(DWaveSampler())

# Find the maximum clique
max_clique = dnx.maximum_clique(G, sampler=sampler)

print("Maximum Clique:", max_clique)

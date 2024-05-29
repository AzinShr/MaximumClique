# MaximumClique
 Maximal Clique Problem: Given a small graph with N nodes and E edges, the task is to find the maximum clique. A clique is a complete subgraph of a given graph. This means that all nodes in the subgraph are directly connected, or there is an edge between any two nodes. The maximal clique is the complete subgraph of a given graph which contains the maximum number of nodes.
 
Example:

Input: N = 4, edges= {{1, 2}, {2, 3}, {3, 1}, {4, 3}, {4, 1}, {4, 2}} 

Output: 4

Steps:
1. **Random Graph Creation**:
   - A random graph `G` is created using `networkx`'s , which generates a graph with `num_nodes` nodes and edges created with probability `edge_prob`.

2. **Sampler Setup**:
   - The `EmbeddingComposite` and `DWaveSampler` are used to set up the sampler to interface with the D-Wave quantum computer.

3. **Finding Maximum Clique**:
   - The `dnx.maximum_clique` function is called with the randomly generated graph `G` and the `sampler` to find the maximum clique.

4. **Result Output**:
   - The maximum clique found in the graph is printed.

You can adjust the `num_nodes` and `edge_prob` variables to create different sizes and densities of random graphs. This code will generate a random graph each time it is run and find the maximum clique in that graph.

----------------
maximum_clique(G, sampler=None, lagrange=2.0, **sampler_args)[source]
Returns an approximate maximum clique. A clique in an undirected graph, G = (V, E), is a subset of the vertex set such that for every two vertices in C, an edge exists connecting the two. This is equivalent to saying that the subgraph induced by C is complete (in some cases, the term clique may also refer to the subgraph). A maximum clique is one of the largest possible sizes in a given graph.

This function works by finding the maximum independent set of the complement graph of the given graph G which is equivalent to finding the maximum clique. It defines a QUBO with ground states corresponding to a maximum weighted independent set and uses the sampler to sample from it.

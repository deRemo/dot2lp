#!/usr/bin/python3
import networkx as nx
import sys

G = nx.drawing.nx_pydot.read_dot("test1.dot")

if not nx.is_directed_acyclic_graph(G):
    sys.exit(-1)


with open("test1.lp", "w") as f:
    # Vertex info constraints
    for v in list(G.nodes(data=True)):
        f.write(f"V_{v[0]}_c = {v[1]['c']}\n")
        f.write(f"V_{v[0]}_M = {v[1]['M']}\n\n")

    # Edge constraints
    f.write("\\ Use as conditional constraints\n")
    for e in list(nx.edge_bfs(G)):
        f.write(f"ADJ_{e[0]}_{e[1]} = 1\n")


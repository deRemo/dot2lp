#!/usr/bin/python3
import networkx as nx
import sys

G = nx.drawing.nx_pydot.read_dot("test1.dot")

if not nx.is_directed_acyclic_graph(G):
    sys.exit(-1)


with open("test1.lp", "w") as f:
    f.write("\\ Use as conditional constraints\n")
    for e in list(nx.edge_bfs(G)):
        f.write(f"ADJ_{e[0]}_{e[1]} = 1\n")


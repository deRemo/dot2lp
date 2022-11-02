#!/usr/bin/python3
import networkx as nx
import sys

if len(sys.argv) != 2:
    print(f"USAGE: {sys.argv[0]} /path/to/file.dot")
    sys.exit(-1)

dotpath = sys.argv[1]
assert ".dot" in dotpath, "Pass a valid .dot file"

G = nx.drawing.nx_pydot.read_dot(dotpath)

if not nx.is_directed_acyclic_graph(G):
    sys.exit(-1)


lppath = dotpath.replace(".dot", ".lp")
with open(lppath, "w") as f:
    # Vertex info constraints
    for v in list(G.nodes(data=True)):
        f.write(f"V_{v[0]}_c = {v[1]['c']}\n")
        f.write(f"V_{v[0]}_M = {v[1]['M']}\n\n")

    # Edge constraints
    f.write("\\ Use as indicator constraints\n")
    for e in list(nx.edge_bfs(G)):
        f.write(f"ADJ_{e[0]}_{e[1]} = 1\n")


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
    f.write("\\ Use the edge constraints as indicator constraints\n")

    f.write("Subject To\n")

    # Vertex info constraints
    for v in list(G.nodes(data=True)):
       for k, val in v[1].items():
           f.write(f" V_{v[0]}_{k} = {v[1][k]}\n")
       f.write("\n")

    # Edge constraints
    for e in list(nx.edge_bfs(G)):
        f.write(f" ADJ_{e[0]}_{e[1]} = 1\n")


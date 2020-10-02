import graphviz
import networkx

def viz(edges: list):
    graph = networkx.DiGraph()
    for edge in edges:
        graph.add_edge(*edge)


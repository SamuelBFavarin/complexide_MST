#!/usr/bin/python3

import numpy as np
from graph import Graph


def smallerEdge(graph: Graph, Q: set):
    smaller = None
    cWeight = 0
    for edge in Q:
        w = graph.get_weight(edge[0], edge[1])
        if w and (w < cWeight or not smaller):
            smaller = edge
            cWeight = w
    return smaller
    
def get_forest(node: int, F: set) -> frozenset:
    for f in F:
        if node in f:
            return f
    return None

def kruskal(graph: Graph):
    S = set()
    Q = set(graph.get_all_edges())
    F = set( frozenset({x}) for x in range(graph.get_nNodes()) )
    while len(Q) != 0:
        a = smallerEdge(graph, Q)
        Q = Q.difference({a})
        Fu = get_forest(a[0], F)
        Fv = get_forest(a[1], F)
        if Fu != Fv:
            S = S.union({a})
            f = Fu.union(Fv)
            F = F.difference({Fu, Fv})
            F = F.union({f})
    return S
    
if __name__ == '__main__':
    graph = Graph('costa/strike.net')
    print(kruskal(graph))


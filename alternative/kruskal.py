#!/usr/bin/python3

import numpy as np
from alternative.graph import Graph
from time import time

def smallerEdge(graph: Graph, Q: set):
    smaller = None
    cWeight = 0
    for edge in Q:
        w = graph.get_weight(edge[0], edge[1])
        if w and (w < cWeight or not smaller):
            smaller = edge
            cWeight = w
    return smaller
    
def get_tree(node: int, F: set) -> frozenset:
    for t in F:
        if node in t:
            return t
    return None

def kruskal(graph: Graph):
    timeTest = 0
    S = set()
    Q = set(graph.get_all_edges())
    F = set( frozenset({x}) for x in range(graph.get_nNodes()) )
    while len(Q) > 0 and len(F) > 1:
        a = smallerEdge(graph, Q)
        Q = Q.difference({a})
        Tu = get_tree(a[0], F)
        Tv = get_tree(a[1], F)
        if Tu != Tv:
            S = S.union({a})
            f = Tu.union(Tv)
            F = F.difference({Tu, Tv})
            F = F.union({f})
    return S



def kruskalSorted(graph: Graph):
    timeTest = 0
    S = set()
    Q = sorted(graph.get_all_edges(), key=lambda e: graph.get_weight(e[0],e[1]))
    F = set( frozenset({x}) for x in range(graph.get_nNodes()) )
    while len(Q) > 0 and len(F) > 1:
        a = Q.pop()
        Tu = get_tree(a[0], F)
        Tv = get_tree(a[1], F)
        if Tu != Tv:
            S = S.union({a})
            f = Tu.union(Tv)
            F = F.difference({Tu, Tv})
            F = F.union({f})
    return S
    
if __name__ == '__main__':
    graph = Graph('costa/strike.net')
    print(kruskal(graph))


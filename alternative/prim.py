#!/usr/bin/python3

import numpy as np
from alternative.graph import Graph


def smallerEdge(graph: Graph, Q: set):
    smaller = None
    cWeight = 0
    for a in Q:
        for b in set(range(graph.get_nNodes())).difference(Q):
            w = graph.get_weight(a, b)
            if w and (w < cWeight or not smaller):
                smaller = (a, b)
                cWeight = w
    return smaller


def prim(graph: Graph):
    S = set()
    Q = set(range(graph.get_nNodes()))
    a = 0
    Q = Q.difference({a})
    while len(Q) != 0:
        a = smallerEdge(graph, Q)
        #if not a:
        #    print('should have stopped', Q)
        #    print(S)
        S = S.union({a})
        Q = Q.difference({ a[0], a[1] })
    return S
    
if __name__ == '__main__':
    graph = Graph('costa/strike.net')
    print(prim(graph))



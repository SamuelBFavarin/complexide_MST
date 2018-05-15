#!/usr/bin/python3

from alternative.graph import Graph
from alternative.kruskal import kruskal, kruskalSorted
from alternative.prim import prim

from time import time

print('Loading')
graph = Graph('normalizadas/jazz.net')
print('size: N(' + str(graph.get_nNodes()) + ') E(' + str(graph.get_nEdges()) + ')')

start = time()
primSol = prim(graph)
primTime = time() - start

start = time()
kruskalSol = kruskal(graph)
kruskalTime = time() - start

start = time()
kruskalSortedSol = kruskalSorted(graph)
kruskalSortedTime = time() - start

def get_cost(sol):
    return sum([ graph.get_weight(e[0], e[1]) for e in sol ])

print('Prim:', get_cost(primSol), 'Time:', primTime)

print('Kruskal:', get_cost(kruskalSol), 'Time:', kruskalTime)

print('KruskalSorted:', get_cost(kruskalSortedSol), 'Time:', kruskalSortedTime)

#print('Solution:')
#for e in sorted(primSol, key=lambda e: (min(e[0], e[1]), max(e[0], e[1]))  ):
#    print(min(e[0],e[1])+1, '->', max(e[0],e[1])+1)

#print('Comparing solutions')
#for edge in primSol:
#    if edge not in kruskalSol and edge[::-1] not in kruskalSol:
#        print('not equal', edge)

#for edge in kruskalSol:
#    if edge not in primSol and edge[::-1] not in primSol:
#        print('not equal', edge)


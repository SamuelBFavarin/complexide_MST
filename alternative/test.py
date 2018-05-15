#!/usr/bin/python3

from graph import Graph
from kruskal import kruskal
from prim import prim

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

print('Prim:', sum([ graph.get_weight(e[0], e[1]) for e in primSol ]), 'Time:', primTime)
print('Kruskal:', sum([ graph.get_weight(e[0], e[1]) for e in kruskalSol ]), 'Time:', kruskalTime)


#print('Comparing solutions')
#for edge in primSol:
#    if edge not in kruskalSol and edge[::-1] not in kruskalSol:
#        print('not equal', edge)

#for edge in kruskalSol:
#    if edge not in primSol and edge[::-1] not in primSol:
#        print('not equal', edge)


#!/usr/bin/python3

import grafo
from time import time

print('Loading')
grafo.load_graph('normalizadas/jazz.net')
print('size: N(' + str(len(grafo.nodes)) + ') E(' + str(len(grafo.edges)/2) + ')')

start = time()
solPrim, costPrim = grafo.prim()
primTime = time() - start

print('Prim:', costPrim, 'Time:', primTime)

start = time()
solKruskal, costKruskal = grafo.kruskal()
kruskalTime = time() - start

print('Kruskal:', costKruskal, 'Time:', kruskalTime)


#print('Comparing solutions')
#for edge in primSol:
#    if edge not in kruskalSol and edge[::-1] not in kruskalSol:
#        print('not equal', edge)

#for edge in kruskalSol:
#    if edge not in primSol and edge[::-1] not in primSol:
#        print('not equal', edge)


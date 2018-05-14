#!/usr/bin/python3

from sys import stdout
import numpy as np


class Graph:
    def __init__(self, filename):
        self.nNodes = 0
        self.labels = []
        with open('../graphs/'+filename) as file:
            lines = file.read().splitlines()
            self.nNodes = int(lines[0].split(' ')[1])
            for line in lines[1:self.nNodes]:
                data = line.split(' ')
                self.labels.append( data[1][1:-1] )

            self._matrix = np.zeros((self.nNodes, self.nNodes))

            self.nEdges = 0
            for line in lines[self.nNodes+2:]:
                data = [int(d) for d in line.split(' ')]
                self.set_weight(data[0]-1, data[1]-1, data[2])
                self.nEdges += 1

    def get_nNodes(self):
        return self.nNodes

    def get_nEdges(self):
        return self.nEdges

    def set_weight(self, node1: int, node2: int, weight: float):
        a = min(node1, node2)
        b = max(node1, node2)
        self._matrix[a][b] = weight

    def get_weight(self, node1: int, node2: int) -> float:
        a = min(node1, node2)
        b = max(node1, node2)
        return self._matrix[a][b]

    def get_all_edges(self):
        for i in range(self.nNodes):
            for j in range(self.nNodes):
                w = self.get_weight(i, j)
                if i > j and w:
                    yield (i,j)

    def print_matrix(self):
        for node in self._matrix:
            for weight in node:
                stdout.write(' ' + str(int(weight)))
            print()


if __name__ == '__main__':
    graph = Graph('costa/galesburg_d.net')
    graph.print_matrix()


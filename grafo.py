##Gerando grafo em matriz de adjacencia
nodes = []
edges = []

def insertNode(node):
    nodes.append(node)

def insertEdgesDirect(n1,n2,weight):
    edge = [n1,n2,weight]
    edges.append(edge)

def insertEdges(n1,n2,weight):
    edge = [n1,n2,weight]
    edges.append(edge)
    edge = [n2,n1,weight]
    edges.append(edge)


def printGraph(nodes, edges):
    print('nodes: ')
    for n in nodes:
        print(n)
    print('edges')
    for e in edges:
        print(e[0], ' -> ', e[1], ' : ', e[2])


def prim():
    s = []
    q = nodes[:]
    nq = []
    a = q[0]
    q.remove(a)
    nq.append(a)
    #min_edges = edges[1]
    while(len(q) > 0):
        min_edges = None
        for e in edges:
            if e[0] in q and e[1] in nq:
                if not min_edges or min_edges[2] > e[2]:
                    #print(min_edges, e)
                    min_edges = e

        s.append(min_edges)
        nq.append(min_edges[0])
        q.remove(min_edges[0])

    #print('Árvore geradora mínima Prim:')
    #for i in s:
    #    print(i)

    sum = 0
    for h in s:
        sum+= h[2]

    return s, sum


#aux functions for kruskal
def findNodeInFlorest(f,node1,node2):
    #err = 0
    for tree in f:
        if node1 in tree and node2 in tree:
            return True
    #    try:
    #        if ( j.index(node1) > -1 and j.index(node2) > -1):
    #            return True
    #    except:
    #        err+= 1
    return False

def unionFlorest(f, node1, node2):
    a = 0
    b = 0
    #print('Nodos: ', node1 , node2)
    #print('Floresta inicial: ', f)

    for i in range(len(f)):
        if node1 in f[i]:
            a = i
        if node2 in f[i]:
            b = i

    a_aux = f[a]
    b_aux = f[b]

    del f[max(a,b)]
    del f[min(a,b)]

    #print('soma de nodos: ', a_aux + b_aux)
    f.append(a_aux + b_aux)
    #print('floresta final: ', f)


    return f


def kruskal():
    s = []
    q = edges[::2]
    f = []
    for i in nodes: f.append([i])

    while(len(q) > 0 and len(f) > 1):
        min_edge = q[0]
        for i in q[1:]:
            if(i[2] < min_edge[2]):
                min_edge = i
        q.remove(min_edge)
        if(findNodeInFlorest(f,min_edge[0],min_edge[1]) == False):
            s.append(min_edge)
            f = unionFlorest(f, min_edge[0], min_edge[1])

    sum = 0
    for h in s:
        sum+= h[2]


    #print('Conjunto s: ',s)

    #print(f)
    #print(sorted(f[0]))
    return s, sum

"""
insertNode('A')
insertNode('B')
insertNode('C')
insertNode('D')
insertNode('E')
insertNode('F')

insertEdges('A','C', 7)
insertEdges('A','D', 2)
insertEdges('A','E', 10)
insertEdges('B','C', 3)
insertEdges('B','F', 2)
insertEdges('C','E', 9)
insertEdges('C','F', 3)
insertEdges('D','E', 7)
insertEdges('D','F', 4)
insertEdges('E','F', 8)
"""

def load_graph(filename):
    del nodes[:]
    del edges[:]
    with open('graphs/'+filename) as file:
        lines = file.read().splitlines()
        nNodes = int(lines[0].split(' ')[1])
        for line in lines[1:nNodes+1]:
            data = line.split(' ')
            insertNode(data[0])

        for line in lines[nNodes+2:]:
            data = line.split(' ')
            insertEdges(data[0], data[1], float(data[2]))


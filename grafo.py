##Gerando grafo em matriz de adjacencia
big_number = 99**9999
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
    a = q[2]
    q.remove(a)
    nq.append(a)
    min_edges = edges[1]
    while(len(q) > 0):
        min_edges = ['X', 'X', big_number] #gambis
        for e in edges:
            for i in q:
                for j in nq:
                    if(e[0] == i and e[1] == j):
                        if (min_edges[2] > e[2]):
                            #print(min_edges, e)
                            min_edges = e

        s.append(min_edges)
        nq.append(min_edges[0])
        q.remove(min_edges[0])

    print('Árvore geradora mínima Prim:')
    for i in s:
        print(i)


#aux functions for kruskal
def findNodeInFlorest(f,node1,node2):
    err = 0
    for j in f:
        try:
            if ( j.index(node1) > -1 and j.index(node2) > -1):
                return True
        except:
            err+= 1
    return False

def unionFlorest(f, node1, node2):
    err = 0
    a = 0
    b = 0
    pos = 0
    #print('Nodos: ', node1 , node2)
    #print('Floresta inicial: ', f)
    for j in f:
        try:
            if (j.index(node2) > -1):
                b = pos
        except ValueError:
            err += 1
        try:
            if (j.index(node1) > -1):
                a = pos
        except ValueError:
            err +=1

        pos+=1


    a_aux = f[a]
    b_aux = f[b]

    for k in f:
        try:
            #print('pos node2: ', k.index(node2))
            if (k.index(node2) >=0):
                f.remove(k)
                #print('Removendo nodo 2: ', f)
        except:
            err += 1

    for k in f:
        try:
            #print('pos node1: ', k.index(node1))
            if (k.index(node1) >=0):
                f.remove(k)
                #print('Removendo nodo 1: ' ,f)
        except:
            err+=1

    #print('soma de nodos: ', a_aux + b_aux)
    f.append(a_aux + b_aux)
    #print('floresta final: ', f)


    return f


def kruskal():
    s = []
    q = edges[::2]
    f = []
    for i in nodes: f.append([i])

    while(len(q) > 0 or len(f) > 1):
        min_edge = q[0]
        for i in q:
            if(i[2] < min_edge[2]):
                min_edge = i
        q.remove(min_edge)
        if(findNodeInFlorest(f,min_edge[0],min_edge[1]) == False):
            s.append(min_edge)
            #print(s)
            f = unionFlorest(f, min_edge[0], min_edge[1])

    sum = 0
    for h in s:
        sum+= h[2]


    print('Conjunto s: ',s)
    print('Peso: ', sum)

    #print(f)
    #print(sorted(f[0]))


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

#prim()

#kruskal()


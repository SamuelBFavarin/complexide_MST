import matplotlib.pyplot as plt
import numpy as np
import math
range = np.arange(0,500, 1)

def prim(n,m):
    return n * m - m

def kruskal(n,m):
    #return ( m**2 - m )/2.0
    return m + m * math.log2(m)

n = 10000

def m_val(n):
    return (n**2)

range = np.arange(1, n, 1)
plt_prim =    [ prim   ( i, m_val(i) ) for i in range ]
plt_kruskal = [ kruskal( i, m_val(i) ) for i in range ]

pr_plt, = plt.plot(plt_prim, label="Prim")
kr_plt, = plt.plot(plt_kruskal, label="Kruskal")

plt.legend(handles=[pr_plt,kr_plt])

plt.title('Complexidade com um grafo esparso (m = n * 1%)')

plt.xlabel('Tamanho de n')
plt.ylabel('Complexidade')

plt.show()


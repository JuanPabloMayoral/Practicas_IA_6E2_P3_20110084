#Juan Pablo Mayoral Lopez 20110084 6E2
#Practica 3 del tercer parcial  Busqueda de profundidad ejemplo 

from collections import deque

# Una clase para representar un objeto grafo
class Graph:
     #Const
    def __init__(self, edges, n):
 
#Listas de adyacencia
        self.adjList = [[] for _ in range(n)]
 
#Se agregan bordes al grafo
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Realizar DFS 
def iterativeDFS(graph, v, discovered):
 
# crea una stack
    stack = deque()
 
# inserta el nodo de origen en la stack
    stack.append(v)
 
# Bucle, hasta que la stack esté vacía
    while stack:
 
# Extrae un vértice de la stack
        v = stack.pop()
 
        # si el vértice ya está descubierto, ignóralo
        if discovered[v]:
            continue
 
        # llegaremos aquí si el vértice reventado `v` aún no se descubre;
        # imprime `v` y procesa sus nodos adyacentes no descubiertos en la stack
        discovered[v] = True
        print(v, end=' ')
 
        # do para cada arista (v, u)
        adjList = graph.adjList[v]
        for i in reversed(range(len(adjList))):
            u = adjList[i]
            if not discovered[u]:
                stack.append(u)
 
 
if __name__ == '__main__':
 
    edges = [
  
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)

    ]
 
    # número total de nodos en el graph (etiquetados de 0 a 12)
    n = 13
 
    # construye un grafo a partir de los bordes dados
    graph = Graph(edges, n)
 
    # para realizar un seguimiento de si se descubre un vértice o no
    discovered = [False] * n
 

    for i in range(n):
        if not discovered[i]:
            iterativeDFS(graph, i, discovered)

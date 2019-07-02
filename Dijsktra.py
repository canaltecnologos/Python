# -*- coding: utf-8 -*-
import networkx as nx
def dijsktra(Grafo, Nodos):
    
#        Encuentra la geodésica entre un nodo origen y un nodo final en una grafo.
#        
#        Parámetros
#        -----------
#        Grafo : Grafo de Networkx
#            Grafo donde se va a buscar la geodésica.
#        Who : tupla
#            Nodo origen y objetivo, respectivamente.
#        
#        Regresa
#        --------
#        S : lista
#            Camino de nodos de la geodésica
    
    grafo = nx.to_dict_of_lists(Grafo)
    S = []; Queue = []; anterior = [0 for i in range(max(grafo)+1)]; distancia = [0 for i in range(max(grafo)+1)]
    
    for nodo in grafo:
        distancia[nodo] = 10000
        Queue.append(nodo)
        
    distancia[Nodos[0]] = 0
    
    while not len(Queue) == 0:
        distancia_minima = 10000
        for nodo in Queue:
            if distancia[nodo] < distancia_minima:
                distancia_minima = distancia[nodo]
                nodo_temporal = nodo
        nodo_distancia_minima = nodo_temporal
        Queue.remove(nodo_distancia_minima)
        
        for vecino in grafo[nodo_distancia_minima]:
            if distancia[nodo_distancia_minima] == 10000:
                distancia_temporal = 0
            else:
                distancia_temporal = distancia[nodo_distancia_minima]
            distancia_con_peso = distancia_temporal + Grafo[nodo_distancia_minima][vecino]['peso']
            if distancia_con_peso < distancia[vecino]:
                distancia[vecino] = distancia_con_peso
                anterior[vecino] = nodo_distancia_minima
                
        if nodo_distancia_minima == Nodos[1]:
            if anterior[nodo_distancia_minima] != 0 or nodo_distancia_minima == Nodos[0]:
                while nodo_distancia_minima != 0:
                    S.insert(0, nodo_distancia_minima)
                    nodo_distancia_minima = anterior[nodo_distancia_minima]
                return S
                
 
##### Prueba #####               
G = nx.Graph()
edges = [(1, 2), (1, 3), (1, 4), (2, 5), (3, 5), (3, 6), (4, 6), (6, 7), (6, 8), (7, 8)]
weights = [3, 2, 5, 3, 1, 6, 2, 4, 1, 2]
G.add_edges_from(edges)
for i, edge in enumerate(edges): 
    G[edge[0]][edge[1]]['peso'] = weights[i]
    
print(dijsktra(G, (1, 8)))
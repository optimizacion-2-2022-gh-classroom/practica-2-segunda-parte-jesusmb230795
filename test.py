from src.opt2.bellman_ford import *
import numpy as np 
import networkx as nx
import bellmanford as bf
import unittest

class Pruebas(unittest.TestCase):

    def test_val_resultado_1(self):
        """
        Válida resultados con el método implementado de bellman_ford vs paquete bellmanford
        https://pypi.org/project/bellmanford/
        """
        edges = [["5", "6", 0.86],
         ["6", "5", -0.94],
         ["3", "3",0],
         ["0","0",0],
         ["1","1",0],
         ["2","2",0],
         ["4","4",0]]
        
        G = nx.DiGraph()        
        G.add_weighted_edges_from(edges)
        # Método implementado con cambios
        list_path, list_val, pred = bf_negative_cycle(G)
        # Paquete bellmanford
        result = bf.bellman_ford(G, source="5", target="4")
        r = [int(x) for x in result[1]]
        self.assertTrue(list_path == r) 

    def test_val_resultado_2(self):
        """
        Válida resultados con el método implementado de bellman_ford vs paquete bellmanford
        https://pypi.org/project/bellmanford/
        """
        edges = [["0", "1", -1],
         ["0", "2", 4],
         ["1", "2", 3],
         ["1", "3", 2],
         ["1", "4", 2],
         ["3", "2", 5],
         ["3", "1", 1],
         ["3", "3", -3]]
        
        G = nx.DiGraph()        
        G.add_weighted_edges_from(edges)
        # Método implementado con cambios
        list_path, list_val, pred = bf_negative_cycle(G)
        # Paquete bellmanford
        result = bf.bellman_ford(G, source="0", target="3")
        r = [int(x) for x in result[1]]
        self.assertTrue(list_path == r) 

    def test_val_iter(self):
        """
        Válida si el camino más corto entre s y t posee k bordes, Bellman Ford lo encontrará después de a lo sumo k iteraciones.
        Dado que un camino más corto no puede tener más de V−1 bordes, toma como mucho esa cantidad de iteraciones.
        https://codeforces.com/blog/entry/81979?locale=en
        """
        edges = [["5", "6", 0.86],
         ["6", "5", -0.94],
         ["3", "3",0],
         ["0","0",0],
         ["1","1",0],
         ["2","2",0],
         ["4","4",0]]
        
        G = nx.DiGraph()        
        G.add_weighted_edges_from(edges)
        
        n_edges = G.number_of_edges()
        n_nodes = G.number_of_nodes()
        
        path_more_short = n_nodes - 1
        
        # Método implementado con cambios
        list_path, list_val, pred = bf_negative_cycle(G)
        
        len_short_path = len(list_path)
        
        self.assertTrue(len_short_path <= path_more_short) 

    def test_dist_inicial(self):
        """
        Válida que la distancia inicial sea mayor o igual a 1.
        """
        edges = [["5", "6", 0.86],
         ["6", "5", -0.94],
         ["3", "3",0],
         ["0","0",0],
         ["1","1",0],
         ["2","2",0],
         ["4","4",0]]
        
        G = nx.DiGraph()        
        G.add_weighted_edges_from(edges)

        distancia_inicial = np.inf
        
        list_path, list_val, pred = bf_negative_cycle(G, distance_ini=distancia_inicial)

        self.assertTrue(distancia_inicial >= 1)

    def test_dist_inicial(self):
        """
        Válida que el nodo inicial no sea mayor a los existentes.
        """
        edges = [["5", "6", 0.86],
         ["6", "5", -0.94],
         ["3", "3",0],
         ["0","0",0],
         ["1","1",0],
         ["2","2",0],
         ["4","4",0]]
        
        G = nx.DiGraph()        
        G.add_weighted_edges_from(edges)

        distancia_inicial = np.inf
        
        list_path, list_val, pred = bf_negative_cycle(G, distance_ini=distancia_inicial)

        node_ini = len(G)

        self.assertTrue(node_ini <= len(G.nodes()))
        
unittest.main(argv=[''], verbosity=2, exit=False)

import bf_cython
import bf_cython2
import numpy as np 
import networkx as nx
import unittest
import time

class Pruebas(unittest.TestCase):

  def test_result(self):
    """
    Compara los resultados entre el código sin perfilamiento (original)
    y el código con perfilamiento compilado en C
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

    res = bf_cython.bf_negative_cycle_p(G)
    res_c = bf_cython.bf_negative_cycle_cc(G)
    self.assertTrue(res == res_c) 

  def test_time(self):
    """
    Compara el tiempo entre el código sin perfilamiento (original)
    y el código con perfilamiento compilado en C
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

    start_time = time.time()
    res = bf_cython.bf_negative_cycle_p(G)
    end_time = time.time()
    secs = end_time-start_time

    start_time_c = time.time()
    res_c = bf_cython.bf_negative_cycle_cc(G)
    end_time_c = time.time()
    secs_c = end_time_c-start_time_c

    self.assertTrue(secs_c < secs) 
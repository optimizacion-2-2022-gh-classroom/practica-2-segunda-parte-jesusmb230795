.. "opt2" documentation master file, created by
   sphinx-quickstart on Sun Mar  7 19:37:05 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Bellman Ford documentation!
==================================

**Bellman Ford algorithm helps us find the shortest path from a vertex to all other vertices of a weighted graph.**


The Bellman-Ford algorithm provides the shortest distance from a prespecified origin node to all other nodes in the graph (weighted digraph). It is able to handle graphs where some of the edge weights are negative numbers. The based idea is: show if there is a negative cycle, generate a negative cycle and always find a negative cycle (if there is one) even if the graph is not connected.

 .. toctree::
   :maxdepth: 1
   :caption: Contents:

   installation
   functions_autosummary

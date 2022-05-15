import numpy as np 

def bf_negative_cycle(graph, node_ini=None, distance_ini=np.inf):
    """
    Description
    -------

    
    Get the shortest path using the Bellman-Ford algorithm, 
    modify parameters monitoring: initial node and initial distance

    
    param:
    -------

    
    G : Networkx DiGraph. The input graph.
    node_ini : Optional parameter, indicate begining node
    distance_ini : Deafault value is inf


    
    returns
    -------


    
    3 list
        A list with the shortest path.
        A list of relaxation
        A list with min spanning tree

        
    """
    assert distance_ini>=1, f"La distancia inicial debe de ser mayor o igual a 1. El parámetro fue igual a {distance_ini}"
    
    if node_ini is None:
        n_nodes = len(graph.nodes())
    else:
        assert node_ini <= len(graph.nodes), f"El nodo definido es mayor a los del grafo. Deberia de ser menor a {len(graph.nodes)}."
        n_nodes = node_ini
            
    n = len(graph.nodes()) + 1
    # Remove nan borders inside graph
    edges = []
    for edge in graph.edges().data():
        if ~np.isnan(edge[2]['weight']):
            edges.append(edge)

    # Add a start node and add zero weighted edges to all other nodes
    for i in range(n-1):
        edges.append((n-1, i, {'weight': 0}))

    # Initialize distances of nodes and predecessors
    distance= np.ones(n) * distance_ini # Starting distances with infinite values
    distance[n_nodes] = 0  # Starting node has zero distance
    predecessors = np.ones(n) * -1  # Starting predecessors with -1 values
    
    list_val=[]

    for i in range(n):  
        x = -1
        for edge in edges:
            if distance[int(edge[0])] + edge[2]['weight'] < distance[int(edge[1])]:                
                a = [distance[int(edge[0])] + edge[2]['weight'], distance[int(edge[1])],predecessors[int(edge[1])],int(edge[1])]
                list_val.append(a)
                distance[int(edge[1])] = distance[int(edge[0])] + edge[2]['weight']
                predecessors[int(edge[1])] = int(edge[0])
                x = int(edge[1])
        if x == -1:  # If relaxation is not possible, there is no negative cycle
            return None
        
    # Identify negative cycle
    for i in range(n):
        x = predecessors[int(x)]
    cycle = []
    v = x
    while True:
        cycle.append(int(v))
        if v == x and len(cycle) > 1:
            break
        v = predecessors[int(v)]
    
    cycle.reverse() # reverse list
    return cycle, list_val, predecessors

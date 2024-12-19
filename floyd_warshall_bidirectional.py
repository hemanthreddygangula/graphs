"""
floyd_warshall.py

This module provides an implementation of the Floyd-Warshall algorithm 
for finding shortest paths in a bidirectional weighted graph.

The module is designed for graphs where edges are bidirectional 
and represented as a list of edges.

Functions:
    floyd_warshall_bidirectional(n, edges)
        Computes the shortest paths between all pairs of nodes in a bidirectional graph.
"""

def floyd_warshall_bidirectional(n, edges):
    """
    Computes the shortest paths between all pairs of nodes in a bidirectional graph.

    Parameters:
    -----------
    n : int
        The number of nodes in the graph, numbered from 0 to n-1.
    edges : list of tuples
        A list of edges, where each edge is represented as a tuple (fromi, toi, weighti).
        - `fromi` and `toi` are the nodes connected by the edge.
        - `weighti` is the weight of the edge.

    Returns:
    --------
    list of lists
        A 2D list (matrix) where the element at [i][j] represents the shortest path
        distance from node `i` to node `j`. If no path exists, the value is `float('inf')`.

    Raises:
    -------
    ValueError
        If a negative weight cycle is detected in the graph.

    Example:
    --------
    >>> n = 4
    >>> edges = [
    ...     (0, 1, 3),
    ...     (0, 3, 5),
    ...     (1, 3, 4),
    ...     (2, 1, 1),
    ...     (3, 2, 2)
    ... ]
    >>> dist = floyd_warshall_bidirectional(n, edges)
    >>> for row in dist:
    ...     print(row)
    [0, 3, 7, 5]
    [3, 0, 3, 4]
    [7, 3, 0, 2]
    [5, 4, 2, 0]
    """
    # Initialize the distance matrix with infinity
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Set the distance from a node to itself to 0
    for i in range(n):
        dist[i][i] = 0
    
    # Populate initial distances based on edges
    for fromi, toi, weighti in edges:
        dist[fromi][toi] = weighti
        dist[toi][fromi] = weighti  # For bidirectional graph
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Check for negative weight cycles
    for i in range(n):
        if dist[i][i] < 0:
            raise ValueError("Graph contains a negative weight cycle")
    
    return dist

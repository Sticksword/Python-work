<<<<<<< HEAD
__author__ = 'Michael - mzc2fd'
from graph import Graph


def is_complete(grph):
    """
    returns true if every node in graph is adjacent to every other node
    """
    if not isinstance(grph, Graph):
        raise TypeError("Input is not a Graph.")
    for node in grph:
        for otherNode in grph:
            if node == otherNode:
                continue
            if not grph.is_adjacent(node, otherNode):
                return False
    return True

def get_key(item):
    return item[1]

def nodes_by_degree(grph):
    """
    returns a sorted list of tuples - each tuple contains the node and the number of adjacent nodes to it
    """
    if not isinstance(grph, Graph):
        raise TypeError("Input is not a Graph.")
    nodes = []
    for node in grph.myDict:
        nodes.append((node, len(grph.myDict[node])))
    nodes.sort(key=get_key, reverse=True)
    #nodes = sorted(nodes, key=get_key, reverse=True)
    # both methods above work in sorting nodes in reverse based on get_key
    return nodes


print is_complete(Graph( { 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] } ))
print nodes_by_degree(Graph( { 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] } ))
=======
__author__ = 'Michael - mzc2fd'
from graph import Graph


def is_complete(grph):
    """
    returns true if every node in graph is adjacent to every other node
    """
    if not isinstance(grph, Graph):
        raise TypeError("Input is not a Graph.")
    for node in grph:
        for otherNode in grph:
            if node == otherNode:
                continue
            if not grph.is_adjacent(node, otherNode):
                return False
    return True

def get_key(item):
    return item[1]

def nodes_by_degree(grph):
    """
    returns a sorted list of tuples - each tuple contains the node and the number of adjacent nodes to it
    """
    if not isinstance(grph, Graph):
        raise TypeError("Input is not a Graph.")
    nodes = []
    for node in grph.myDict:
        nodes.append((node, len(grph.myDict[node])))
    nodes.sort(key=get_key, reverse=True)
    #nodes = sorted(nodes, key=get_key, reverse=True)
    # both methods above work in sorting nodes in reverse based on get_key
    return nodes


print is_complete(Graph( { 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] } ))
print nodes_by_degree(Graph( { 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] } ))
>>>>>>> origin/master
print is_complete(Graph( {'A': ['B', 'E'], 'B': ['A'], 'C': ['D','E'], 'D': ['C'], 'E': ['A', 'C']}))
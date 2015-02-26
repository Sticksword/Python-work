<<<<<<< HEAD
__author__ = 'Michael - mzc2fd'


class Graph:

    def __init__(self, init_values={}):
        """
        constructor that optionally takes in a dictionary used to initialize the graph
        """
        self.myDict = init_values or {}
    #using 'or []' avoids having the same value being pointed to by multiple instances of Queue
    #cannot overload constructors

    def __str__(self):
        """
        returns a string representation of the data in the graph, formatted like a Python dictionary
        """
        return str(self.myDict)

    def __iter__(self):
        """
        returns an iterator that allows user to iterate over the nodes in the graph
        """
        return iter(self.myDict)

    def __contains__(self, item):
        """
        returns true if node is in graph, false if not
        """
        if item in self.myDict.keys():
            return True
        return False

    def __len__(self):
        """
        returns how many nodes are in the graph
        """
        return len(self.myDict.keys())

    def get_adjlist(self, node):
        """
        returns the list of nodes adjacent to parameter node
        """
        if not node in self.myDict.keys():
            return None
        return self.myDict[node]

    def is_adjacent(self, node1, node2):
        """
        returns true if node2 is adjacent to node1
        """
        if node1 not in self.myDict.keys():
            return False
        if node2 in self.get_adjlist(node1):
            return True
        return False

    def num_nodes(self):
        """
        returns how many nodes there are in graph
        """
        return len(self.myDict.keys())

    def addNode(self, node):
        """
        this adds node to the graph if node in't already in graph
        """
        if node in self.myDict.keys():
            return False
        self.myDict.keys().append(node)
        return True

    def link_nodes(self, node1, node2):
        """
        connects two nodes together if they are not already connected (adjacent)
        """
        if not (node1 in self.myDict.keys() and node2 in self.myDict.keys() ):
            return False
        if node1 == node2:
            return False
        if node2 in self.myDict[node1]:
            return False
        self.myDict[node1].append(node2)
        self.myDict[node2].append(node1)
        return True

    def unlink_nodes(self, node1, node2):
        """
        makes two nodes not be connected if both are in the graph
        """
        if not self.is_adjacent(node1, node2):
            return False
        if not (node1 in self.myDict.keys() and node2 in self.myDict.keys() ):
            return False
        self.myDict[node1].remove(node2)
        self.myDict[node2].remove(node1)
        return True

    def del_node(self, node):
        """
        removes a node and all edges to that node if the node is in the graph
        """
        if not node in self.myDict.keys():
            return False
        # self.myDict.keys().remove(node)
        for item in self.myDict[node]:
            self.myDict[item].remove(node)
        del self.myDict[node]
        return True

if __name__ == '__main__':
    g = Graph( { 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] } )
    # print Graph.num_nodes(g), len(g)
    # print g.__len__()
    # print g.__contains__('A')
    # print g.get_adjlist('A')
    # print g.is_adjacent('A', 'B')
    # print "add F?"
    # print g.addNode('F')
    # print "add A?"
    # print g.addNode('A')
    # print "successful link?"
    # print g.link_nodes('A','B')
    # print "successful unlink?"
    # print g.unlink_nodes('A', 'B')
    # print "time to delete?"
=======
__author__ = 'Michael - mzc2fd'


class Graph:

    def __init__(self, init_values={}):
        """
        constructor that optionally takes in a dictionary used to initialize the graph
        """
        self.myDict = init_values or {}
    #using 'or []' avoids having the same value being pointed to by multiple instances of Queue
    #cannot overload constructors

    def __str__(self):
        """
        returns a string representation of the data in the graph, formatted like a Python dictionary
        """
        return str(self.myDict)

    def __iter__(self):
        """
        returns an iterator that allows user to iterate over the nodes in the graph
        """
        return iter(self.myDict)

    def __contains__(self, item):
        """
        returns true if node is in graph, false if not
        """
        if item in self.myDict.keys():
            return True
        return False

    def __len__(self):
        """
        returns how many nodes are in the graph
        """
        return len(self.myDict.keys())

    def get_adjlist(self, node):
        """
        returns the list of nodes adjacent to parameter node
        """
        if not node in self.myDict.keys():
            return None
        return self.myDict[node]

    def is_adjacent(self, node1, node2):
        """
        returns true if node2 is adjacent to node1
        """
        if node1 not in self.myDict.keys():
            return False
        if node2 in self.get_adjlist(node1):
            return True
        return False

    def num_nodes(self):
        """
        returns how many nodes there are in graph
        """
        return len(self.myDict.keys())

    def addNode(self, node):
        """
        this adds node to the graph if node in't already in graph
        """
        if node in self.myDict.keys():
            return False
        self.myDict.keys().append(node)
        return True

    def link_nodes(self, node1, node2):
        """
        connects two nodes together if they are not already connected (adjacent)
        """
        if not (node1 in self.myDict.keys() and node2 in self.myDict.keys() ):
            return False
        if node1 == node2:
            return False
        if node2 in self.myDict[node1]:
            return False
        self.myDict[node1].append(node2)
        self.myDict[node2].append(node1)
        return True

    def unlink_nodes(self, node1, node2):
        """
        makes two nodes not be connected if both are in the graph
        """
        if not self.is_adjacent(node1, node2):
            return False
        if not (node1 in self.myDict.keys() and node2 in self.myDict.keys() ):
            return False
        self.myDict[node1].remove(node2)
        self.myDict[node2].remove(node1)
        return True

    def del_node(self, node):
        """
        removes a node and all edges to that node if the node is in the graph
        """
        if not node in self.myDict.keys():
            return False
        # self.myDict.keys().remove(node)
        for item in self.myDict[node]:
            self.myDict[item].remove(node)
        del self.myDict[node]
        return True

if __name__ == '__main__':
    g = Graph( { 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] } )
    # print Graph.num_nodes(g), len(g)
    # print g.__len__()
    # print g.__contains__('A')
    # print g.get_adjlist('A')
    # print g.is_adjacent('A', 'B')
    # print "add F?"
    # print g.addNode('F')
    # print "add A?"
    # print g.addNode('A')
    # print "successful link?"
    # print g.link_nodes('A','B')
    # print "successful unlink?"
    # print g.unlink_nodes('A', 'B')
    # print "time to delete?"
>>>>>>> origin/master
    # print g.del_node('A')
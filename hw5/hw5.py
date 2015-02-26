__author__ = 'Michael'
from networkx.classes.function import get_edge_attributes
from networkx.algorithms.flow import shortest_augmenting_path

import sys
import networkx as nx

if __name__ == '__main__':
    # G = nx.DiGraph()
    # G.add_edge('x','a', capacity=3.0)
    # G.add_edge('x','b', capacity=1.0)
    # G.add_edge('a','c', capacity=3.0)
    # G.add_edge('b','c', capacity=5.0)
    # G.add_edge('b','d', capacity=4.0)
    # G.add_edge('d','e', capacity=2.0)
    # G.add_edge('c','y', capacity=2.0)
    # G.add_edge('e','y', capacity=3.0)
    # flow_value = nx.maximum_flow(G, 'x', 'y', flow_func=shortest_augmenting_path)
    # print flow_value
    with open(sys.argv[1]) as f:
        GG = []
        G = nx.DiGraph()
        requests = 0
        classes = 0
        req = 0
        for line in f:
            words = line.strip().split(" ")
            if len(words) == 1:  # case when there is empty line - list size is 1 b/c of empty string
                GG.append(G)
                G = nx.DiGraph()
                continue

            if not words[0].isdigit():  # case when there is line that has word at start
                if requests > 0:  # case when there are still requests
                    G.add_edge("s", words[0], capacity=req)  # add edge between s and x
                    G.add_edge(words[0], words[1], capacity=1)  # add edge between x & y
                    requests -= 1
                else:  # case when there are no more requests - time to process classes
                    G.add_edge(words[0], "t", capacity=int(words[1]))  # add edge between y and t

            else:  # case when there is line that has number at start

                if int(words[0]) == 0 and int(words[1]) == 0 and int(words[2]) == 0:
                    break
                else:
                    requests = int(words[0])
                    classes = int(words[1])
                    req = int(words[2])
    for graph in GG:
        flow_value = nx.maximum_flow(graph, "s", "t", capacity='capacity', flow_func=shortest_augmenting_path)
        if flow_value[0] >= req:
            print 'yes'
        else:
            print 'no'
        # print flow_value
        # my_dict = get_edge_attributes(graph, 'capacity')
        # for edge in my_dict:
        #     print edge, my_dict[edge]
from networkx.classes.function import get_edge_attributes

__author__ = 'Michael'

import sys
import networkx as nx


def recursive_dfs(graph, start, path=[]):
    path.append(start)
    print start
    for node in graph[start].keys():
        path.append(recursive_dfs(graph, node, path))
    return path


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        GG = []
        G = nx.DiGraph()
        G.add_node("s")
        G.add_node("t")
        requests = 0
        classes = 0
        req = 0
        for line in f:
            words = line.strip().split(" ")
            if len(words) == 1:  # case when there is empty line - list size is 1 b/c of empty string
                GG.append(G)
                G = nx.DiGraph()
                G.add_node("s")
                G.add_node("t")
                continue

            if not words[0].isdigit():  # case when there is line that has word at start
                if requests > 0:  # case when there are still requests
                    if not words[0] in G.nodes():
                        G.add_node(words[0])  # add node x
                        G.add_edge("s", words[0], residual=req)  # add edge between s and x
                    if not words[1] in G.nodes():
                        G.add_node(words[1])  # add node y
                    G.add_edge(words[0], words[1], residual=1)  # add edge between x & y
                    requests -= 1
                else:  # case when there are no more requests - time to process classes
                    G.add_edge(words[0], "t", residual=int(words[1]))  # add edge between y and t

            else:  # case when there is line that has number at start

                if int(words[0]) == 0 and int(words[1]) == 0 and int(words[2]) == 0:
                    break
                else:
                    requests = int(words[0])
                    classes = int(words[1])
                    req = int(words[2])
    for graph in GG:
        my_dict = get_edge_attributes(graph, 'residual')
        for edge in my_dict:
            print edge, my_dict[edge]
        recursive_dfs(graph, "s", path=[])


        # for node in graph.nodes():
        #     print node, graph[node].keys()





            # stack = [3, 4, 5]
            # stack.append(6)
            # stack.append(7)
            # print stack.pop()
            # print stack
            # A = nx.Graph()
            # A.add_edge(1,3)
            # G[1][3]['weight'] = 5
            # print G[1][3]['weight']

            # G = nx.Graph()
            # H = nx.path_graph(10)
            # G.add_nodes_from(H)
            # print G.number_of_nodes()
            # G.add_edge(1,2)
            # print G.number_of_edges()
            # print G.nodes()
            # print G.edges()
            # print G.neighbors(1)
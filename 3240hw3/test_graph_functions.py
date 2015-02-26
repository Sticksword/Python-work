<<<<<<< HEAD
__author__ = 'Michael - mzc2fd'

import unittest
from graph import Graph
from graph_functions import is_complete, nodes_by_degree


class test_graph_functions(unittest.TestCase):
    def setUp(self):
        self.emptyGraph = Graph()
        self.g1 = Graph( { 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] } )
        self.g2 = Graph( { 'A': ['B'], 'B': ['A']})
        self.g3 = Graph( { 'A': []})

    def test_is_complete_gf1(self):
        self.assertFalse(is_complete(self.g1))

    def test_is_complete_gf2(self):
        self.assertTrue(is_complete(self.g2))

    def test_is_complete_gf3(self):
        self.assertTrue(is_complete(self.g3))

    def test_nodes_by_degree_gf4(self):
        self.assertEqual(nodes_by_degree(self.g1), [('B', 3), ('A', 2), ('D', 2), ('C', 1), ('E', 0)])

    def test_nodes_by_degree_gf5(self):
        self.assertEqual(nodes_by_degree(self.emptyGraph), [])

if __name__ == '__main__':
    unittest.main()
=======
__author__ = 'Michael - mzc2fd'

import unittest
from graph import Graph
from graph_functions import is_complete, nodes_by_degree


class test_graph_functions(unittest.TestCase):
    def setUp(self):
        self.emptyGraph = Graph()
        self.g1 = Graph( { 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] } )
        self.g2 = Graph( { 'A': ['B'], 'B': ['A']})
        self.g3 = Graph( { 'A': []})

    def test_is_complete_gf1(self):
        self.assertFalse(is_complete(self.g1))

    def test_is_complete_gf2(self):
        self.assertTrue(is_complete(self.g2))

    def test_is_complete_gf3(self):
        self.assertTrue(is_complete(self.g3))

    def test_nodes_by_degree_gf4(self):
        self.assertEqual(nodes_by_degree(self.g1), [('B', 3), ('A', 2), ('D', 2), ('C', 1), ('E', 0)])

    def test_nodes_by_degree_gf5(self):
        self.assertEqual(nodes_by_degree(self.emptyGraph), [])

if __name__ == '__main__':
    unittest.main()
>>>>>>> origin/master

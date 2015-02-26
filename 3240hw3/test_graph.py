<<<<<<< HEAD
from nose.tools import assert_false, assert_equals, assert_true

__author__ = 'Michael - mzc2fd'

import unittest
from graph import Graph


class test_graph(unittest.TestCase):
    def setUp(self):
        self.emptyGraph = Graph()
        self.g1 = Graph( { 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] } )

    def test_len_g1(self):
        self.assertEquals(self.g1.__len__(), 5)

    def test_len_g2(self):
        self.assertEquals(self.emptyGraph.__len__(), 0)

    def test_get_adjlist_g3(self):
        self.assertEquals(self.g1.get_adjlist('A'), ['B', 'D'])

    def test_get_adjlist_g4(self):
        self.assertEquals(self.emptyGraph.get_adjlist('E'), None)

    def test_is_adjacent_g5(self):
        self.assertTrue(self.g1.is_adjacent('A', 'B'))

    def test_is_adjacent_g6(self):
        self.assertFalse(self.g1.is_adjacent('A', 'C'))

    def test_num_nodes_g7(self):
        self.assertEquals(self.g1.num_nodes(), 5)

    def test_num_nodes_g8(self):
        self.assertEquals(self.emptyGraph.num_nodes(), 0)

    def test_addNode_g9(self):
        self.assertTrue(self.g1.addNode('F'))

    def test_addNode_g10(self):
        self.assertFalse(self.g1.addNode('A'))

    def test_link_nodes_g11(self):
        self.assertFalse(self.g1.link_nodes('A', 'B'))

    def test_link_nodes_g12(self):
        self.assertTrue(self.g1.link_nodes('A', 'C'))

    def test_link_nodes_g13(self):
        self.assertFalse(self.g1.link_nodes('A', 'Z'))

    def test_link_nodes_g14(self):
        self.assertFalse(self.g1.link_nodes('A', 'A'))

    def test_unlink_nodes_g15(self):
        self.assertTrue(self.g1.unlink_nodes('A', 'B'))

    def test_unlink_nodes_g16(self):
        self.assertFalse(self.g1.unlink_nodes('A', 'F'))

    def test_unlink_nodes_g17(self):
        self.assertFalse(self.g1.unlink_nodes('A', 'Y'))

    def test_del_node_g18(self):
        self.assertTrue(self.g1.del_node('A'))

    def test_del_node_g19(self):
        self.assertFalse(self.g1.del_node('X'))

if __name__ == '__main__':
    unittest.main()
=======
from nose.tools import assert_false, assert_equals, assert_true

__author__ = 'Michael - mzc2fd'

import unittest
from graph import Graph


class test_graph(unittest.TestCase):
    def setUp(self):
        self.emptyGraph = Graph()
        self.g1 = Graph( { 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] } )

    def test_len_g1(self):
        self.assertEquals(self.g1.__len__(), 5)

    def test_len_g2(self):
        self.assertEquals(self.emptyGraph.__len__(), 0)

    def test_get_adjlist_g3(self):
        self.assertEquals(self.g1.get_adjlist('A'), ['B', 'D'])

    def test_get_adjlist_g4(self):
        self.assertEquals(self.emptyGraph.get_adjlist('E'), None)

    def test_is_adjacent_g5(self):
        self.assertTrue(self.g1.is_adjacent('A', 'B'))

    def test_is_adjacent_g6(self):
        self.assertFalse(self.g1.is_adjacent('A', 'C'))

    def test_num_nodes_g7(self):
        self.assertEquals(self.g1.num_nodes(), 5)

    def test_num_nodes_g8(self):
        self.assertEquals(self.emptyGraph.num_nodes(), 0)

    def test_addNode_g9(self):
        self.assertTrue(self.g1.addNode('F'))

    def test_addNode_g10(self):
        self.assertFalse(self.g1.addNode('A'))

    def test_link_nodes_g11(self):
        self.assertFalse(self.g1.link_nodes('A', 'B'))

    def test_link_nodes_g12(self):
        self.assertTrue(self.g1.link_nodes('A', 'C'))

    def test_link_nodes_g13(self):
        self.assertFalse(self.g1.link_nodes('A', 'Z'))

    def test_link_nodes_g14(self):
        self.assertFalse(self.g1.link_nodes('A', 'A'))

    def test_unlink_nodes_g15(self):
        self.assertTrue(self.g1.unlink_nodes('A', 'B'))

    def test_unlink_nodes_g16(self):
        self.assertFalse(self.g1.unlink_nodes('A', 'F'))

    def test_unlink_nodes_g17(self):
        self.assertFalse(self.g1.unlink_nodes('A', 'Y'))

    def test_del_node_g18(self):
        self.assertTrue(self.g1.del_node('A'))

    def test_del_node_g19(self):
        self.assertFalse(self.g1.del_node('X'))

if __name__ == '__main__':
    unittest.main()
>>>>>>> origin/master

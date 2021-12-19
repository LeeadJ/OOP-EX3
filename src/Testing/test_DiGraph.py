from unittest import TestCase

from src.DiGraph import DiGraph


class TestDiGraph(TestCase):

    def test_v_size(self):
        graph_test = DiGraph()
        graph_test.add_node(1, (0, 0, 0))
        graph_test.add_node(2, (0, 0, 0))
        graph_test.add_node(3, (0, 0, 0))
        graph_test.add_node(4, (0, 0, 0))
        graph_test.add_edge(1, 2, 1)
        graph_test.add_edge(1, 3, 1)
        graph_test.add_edge(1, 4, 1)
        graph_test.add_edge(2, 4, 1)
        self.assertEqual(graph_test.v_size(), 4)

    def test_e_size(self):
        graph_test = DiGraph()
        graph_test.add_node(1, (0, 0, 0))
        graph_test.add_node(2, (0, 0, 0))
        graph_test.add_node(3, (0, 0, 0))
        graph_test.add_node(4, (0, 0, 0))
        graph_test.add_edge(1, 2, 1)
        graph_test.add_edge(1, 3, 1)
        graph_test.add_edge(1, 4, 1)
        graph_test.add_edge(2, 4, 1)
        self.assertEqual(graph_test.e_size(), 4)

    def test_all_in_edges_of_node(self):
        graph_test = DiGraph()
        graph_test.add_node(1, (0, 0, 0))
        graph_test.add_node(2, (0, 0, 0))
        graph_test.add_node(3, (0, 0, 0))
        graph_test.add_node(4, (0, 0, 0))
        graph_test.add_edge(1, 2, 1)
        graph_test.add_edge(1, 3, 1)
        graph_test.add_edge(1, 4, 1)
        graph_test.add_edge(2, 4, 1)
        print(graph_test.all_in_edges_of_node(4))

    def test_all_out_edges_of_node(self):
        graph_test = DiGraph()
        graph_test.add_node(1, (0, 0, 0))
        graph_test.add_node(2, (0, 0, 0))
        graph_test.add_node(3, (0, 0, 0))
        graph_test.add_node(4, (0, 0, 0))
        graph_test.add_edge(1, 2, 1)
        graph_test.add_edge(1, 3, 1)
        graph_test.add_edge(1, 4, 1)
        graph_test.add_edge(2, 4, 1)
        print(graph_test.all_out_edges_of_node(1))

    def test_get_mc(self):
        graph_test = DiGraph()
        graph_test.add_node(1, (0, 0, 0))
        graph_test.add_node(2, (0, 0, 0))
        graph_test.add_node(3, (0, 0, 0))
        graph_test.add_node(4, (0, 0, 0))
        graph_test.add_edge(1, 2, 1)
        graph_test.add_edge(1, 3, 1)
        graph_test.add_edge(1, 4, 1)
        graph_test.add_edge(2, 4, 1)
        self.assertEqual(graph_test.mc, 8)

    def test_add_edge(self):
        graph_test = DiGraph()
        self.assertFalse(graph_test.add_edge(1, 2, 1))
        graph_test.add_node(1, (0, 0, 0))
        self.assertFalse(graph_test.add_edge(1, 2, 1))
        graph_test.add_node(2, (0, 0, 0))
        self.assertTrue(graph_test.add_edge(1, 2, 1))

    def test_add_node(self):
        graph_test = DiGraph()
        self.assertTrue(graph_test.add_node(1, (0, 0, 0)))
        self.assertTrue(graph_test.add_node(2, (0, 0, 0)))
        self.assertTrue(graph_test.add_node(3, (0, 0, 0)))
        self.assertTrue(graph_test.add_node(4, (0, 0, 0)))

    def test_remove_node(self):
        graph_test = DiGraph()
        graph_test.add_node(1, (0, 0, 0))
        graph_test.add_node(2, (0, 0, 0))
        graph_test.add_node(3, (0, 0, 0))
        graph_test.add_node(4, (0, 0, 0))
        self.assertTrue(graph_test.remove_node(1))
        self.assertTrue(graph_test.remove_node(2))

    def test_remove_edge(self):
        graph_test = DiGraph()
        graph_test.add_node(1, (0, 0, 0))
        graph_test.add_node(2, (0, 0, 0))
        graph_test.add_node(3, (0, 0, 0))
        graph_test.add_node(4, (0, 0, 0))
        graph_test.add_edge(1, 2, 1)
        graph_test.add_edge(1, 3, 1)
        graph_test.add_edge(1, 4, 1)
        graph_test.add_edge(2, 4, 1)
        self.assertTrue(graph_test.remove_edge(1, 2))
        self.assertTrue(graph_test.remove_edge(2, 4))

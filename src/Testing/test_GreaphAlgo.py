from unittest import TestCase
from src.DiGraph import DiGraph
from src.Gnode import Gnode
from src.GraphAlgo import GraphAlgo
import time


class TestGraphAlgo(TestCase):

    def test_get_graph(self):
        a = Gnode(0, None)
        b = Gnode(1, None)
        c = Gnode(2, None)
        d = Gnode(3, None)
        e = Gnode(4, None)
        graph = DiGraph()
        algo = GraphAlgo(graph)
        algo.get_graph().add_node(a.key, a.location)
        algo.get_graph().add_node(b.key, b.location)
        algo.get_graph().add_node(c.key, c.location)
        algo.get_graph().add_node(d.key, d.location)
        algo.get_graph().add_edge(0, 1, 3.0)
        self.assertEqual(graph, algo.get_graph())

    def test_load_from_json(self):
        graph_test = DiGraph()
        algo = GraphAlgo(graph_test)
        algo.load_from_json(r"C:\Users\Leead\PycharmProjects\OOP-EX3\src\data\A0.json")
        self.assertTrue(algo.load_from_json)
        str = '|V|=11 , |E|=22'
        self.assertTrue(algo.get_graph()._str_() == str)
        algo.load_from_json(r"C:\Users\Leead\PycharmProjects\OOP-EX3\src\data\A5.json")
        self.assertTrue(algo.load_from_json)
        str = '|V|=48 , |E|=166'
        self.assertTrue(algo.get_graph()._str_() == str)

    def test_save_to_json(self):
        a = Gnode(0, None)
        b = Gnode(1, None)
        c = Gnode(2, None)
        d = Gnode(3, None)
        e = Gnode(4, None)
        graph = DiGraph()
        algo = GraphAlgo(graph)
        algo.get_graph().add_node(a.key, a.location)
        algo.get_graph().add_node(b.key, b.location)
        algo.get_graph().add_node(c.key, c.location)
        algo.get_graph().add_node(d.key, d.location)
        algo.get_graph().add_edge(0, 1, 3.0)
        self.assertTrue(algo.save_to_json("Save-Test_Graph"))

    def test_shortest_path(self):
        a = Gnode(0, None)
        b = Gnode(1, None)
        c = Gnode(2, None)
        d = Gnode(3, None)
        e = Gnode(4, None)
        graph = DiGraph()
        algo = GraphAlgo(graph)
        algo.get_graph().add_node(a.key, a.location)
        algo.get_graph().add_node(b.key, b.location)
        algo.get_graph().add_node(c.key, c.location)
        algo.get_graph().add_node(d.key, d.location)
        algo.get_graph().add_edge(0, 1, 3.0)
        algo.get_graph().add_edge(0, 3, 7.0)
        algo.get_graph().add_edge(1, 0, 8.0)
        algo.get_graph().add_edge(1, 2, 2.0)
        algo.get_graph().add_edge(2, 0, 5.0)
        algo.get_graph().add_edge(2, 3, 1.0)
        algo.get_graph().add_edge(3, 0, 2.0)
        llist = [3, 0, 1, 2]
        ans = (7.0, llist)
        self.assertEqual(ans, algo.shortest_path(3, 2))
        print(algo.shortest_path(3, 2))

    def test_center_point(self):
        graph_test = DiGraph()
        algo = GraphAlgo(graph_test)
        algo.load_from_json(r"C:\Users\Leead\PycharmProjects\OOP-EX3\src\data\A0.json")
        A0 = (7, 6.806805834715163)
        self.assertEqual(A0, algo.centerPoint())
        algo.load_from_json(r"C:\Users\Leead\PycharmProjects\OOP-EX3\src\data\A1.json")
        A1 = (8, 9.925289024973141)
        self.assertEqual(A1, algo.centerPoint())
        algo.load_from_json(r"C:\Users\Leead\PycharmProjects\OOP-EX3\src\data\A2.json")
        A2 = (0, 7.819910602212574)
        self.assertEqual(A2, algo.centerPoint())
        algo.load_from_json(r"C:\Users\Leead\PycharmProjects\OOP-EX3\src\data\A3.json")
        A3 = (2, 8.182236568942237)
        self.assertEqual(A3, algo.centerPoint())
        algo.load_from_json(r"C:\Users\Leead\PycharmProjects\OOP-EX3\src\data\A4.json")
        A4 = (6, 8.071366078651435)
        self.assertEqual(A4, algo.centerPoint())
        algo.load_from_json(r"C:\Users\Leead\PycharmProjects\OOP-EX3\src\data\A5.json")
        A5 = (40, 9.291743173960954)
        self.assertEqual(A5, algo.centerPoint())

    def test_plot_graph(self):
        graph_test = DiGraph()
        algo = GraphAlgo(graph_test)
        algo.load_from_json("C:/Users/arieh/PycharmProjects/OOP-EX3/src/data/A5.json")
        algo.plot_graph()

    def test_tsp(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(5):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 4, 5)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(1, 3, 1.9)
        g.add_edge(2, 3, 1.1)
        g.add_edge(3, 4, 2.1)
        g.add_edge(4, 2, .5)
        g_algo = GraphAlgo(g)
        print(g_algo.TSP([1, 2, 4]))

    def test_dijkstraAlgo(self):
        a = Gnode(0, None)
        b = Gnode(1, None)
        c = Gnode(2, None)
        d = Gnode(3, None)
        e = Gnode(4, None)
        graph = DiGraph()
        algo = GraphAlgo(graph)
        algo.get_graph().add_node(a.key, a.location)
        algo.get_graph().add_node(b.key, b.location)
        algo.get_graph().add_node(c.key, c.location)
        algo.get_graph().add_node(d.key, d.location)
        algo.get_graph().add_edge(0, 1, 3.0)
        algo.get_graph().add_edge(0, 3, 7.0)
        algo.get_graph().add_edge(1, 0, 8.0)
        algo.get_graph().add_edge(1, 2, 2.0)
        algo.get_graph().add_edge(2, 0, 5.0)
        algo.get_graph().add_edge(2, 3, 1.0)
        algo.get_graph().add_edge(3, 0, 2.0)
        self.assertEqual(5.0, algo.dijkstraAlgo(0, 2)[0])
        self.assertEqual([0, 1, 2], algo.dijkstraAlgo(0, 2)[1])
        print(algo.dijkstraAlgo(0, 2))
        best = set()
        best.clear()
        best.update(algo.dijkstraAlgo(0, 2)[1])
        best.update(algo.dijkstraAlgo(0, 3)[1])
        print(best)

    def runtime_checker(self):
        g1 = r"C:\Users\Leead\PycharmProjects\OOP-EX3\src\data\G1.json"
        g2 = r"C:\Users\Leead\PycharmProjects\OOP-EX3\src\data\G2.json"
        g3 = r"C:\Users\Leead\PycharmProjects\OOP-EX3\src\data\G3.json"
        graphs = (g1, g2, g3)
        for g in graphs:
            graph = DiGraph(g)
            algo = GraphAlgo(graph)

            start_time = time.time()
            algo.centerPoint()
            finish_time = time.time()
            center = finish_time - start_time

            start_time = time.time()

            finish_time = time.time()
            center = finish_time - start_time
        algo.load_from_json("C:/Users/arieh/PycharmProjects/OOP-EX3/src/data/A5.json")



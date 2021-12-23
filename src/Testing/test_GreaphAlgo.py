from unittest import TestCase
from src.DiGraph import DiGraph
from src.Gnode import Gnode
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_load_from_json(self):
        graph_test = DiGraph()
        algo = GraphAlgo(graph_test)
        algo.load_from_json(r"C:\Users\arieh\PycharmProjects\OOP-EX3\src\data\T0.json")
        print(algo.get_graph())
        # print(algo.get_graph().get_all_v().get(0).location)
        # algo.save_to_json("test_output.json")

    def test_shortest_path(self):
        n0 = Gnode(0, None)
        n1 = Gnode(5, None)
        n2 = Gnode(2, None)
        n3 = Gnode(3, None)
        g = DiGraph()

        g.add_node(n0.key, n0.location)
        g.add_node(n1.key, n1.location)
        g.add_node(n2.key, n2.location)
        g.add_node(n3.key, n3.location)

        g.add_edge(0, 5, 1)
        g.add_edge(0, 2, 4)
        g.add_edge(5, 2, 2)
        g.add_edge(5, 3, 6)
        g.add_edge(2, 3, 3)

        algo = GraphAlgo(g)
        print(algo.get_graph())
        print(algo.shortest_path(0, 3))

    def test_center_point(self):
        graph_test = DiGraph()
        algo = GraphAlgo(graph_test)
        algo.load_from_json(r"C:\Users\arieh\PycharmProjects\OOP-EX3\src\data\A0.json")
        print(algo.centerPoint())
        algo.load_from_json(r"C:\Users\arieh\PycharmProjects\OOP-EX3\src\data\A1.json")
        print(algo.centerPoint())
        algo.load_from_json(r"C:\Users\arieh\PycharmProjects\OOP-EX3\src\data\A2.json")
        print(algo.centerPoint())
        algo.load_from_json(r"C:\Users\arieh\PycharmProjects\OOP-EX3\src\data\A3.json")
        print(algo.centerPoint())
        algo.load_from_json(r"C:\Users\arieh\PycharmProjects\OOP-EX3\src\data\A4.json")
        print(algo.centerPoint())
        algo.load_from_json(r"C:\Users\arieh\PycharmProjects\OOP-EX3\src\data\A5.json")
        print(algo.centerPoint())

    def test_plot_graph(self):
        graph_test = DiGraph()
        algo = GraphAlgo(graph_test)
        algo.load_from_json("C:/Users/arieh/PycharmProjects/OOP-EX3/src/data/A5.json")
        algo.plot_graph()

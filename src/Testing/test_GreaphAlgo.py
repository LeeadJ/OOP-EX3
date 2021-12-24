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
        graph_test = DiGraph()
        algo = GraphAlgo(graph_test)
        algo.load_from_json(r"C:\Users\arieh\PycharmProjects\OOP-EX3\src\data\A1.json")
        for n in algo.graph.node_map.values():
            print(n)

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

    def test_is_connected(self):
        graph_test = DiGraph()
        algo = GraphAlgo(graph_test)
        algo.load_from_json(r"C:\Users\arieh\PycharmProjects\OOP-EX3\src\data\A1.json")
        self.assertTrue(algo.isConnected())
        graph_test1 = DiGraph()
        graph_test1.add_node(0, (0, 0, 0))
        graph_test1.add_node(1, (0, 0, 0))
        algo1 = GraphAlgo(graph_test1)
        self.assertFalse(algo1.isConnected())

    def test_tsp(self):
        graph_test = DiGraph()
        algo = GraphAlgo(graph_test)
        algo.load_from_json(r"C:\Users\arieh\PycharmProjects\OOP-EX3\src\data\A1.json")
        # algo.plot_graph()
        list_tsp = [5, 6, 2, 3, 4]
        print(algo.TSP(list_tsp))

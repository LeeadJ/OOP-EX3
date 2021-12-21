import heapq
import json
import math
from typing import List

from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import *


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'r') as json_file:
                json_load = json.load(json_file)
                graph = DiGraph()
                for node in json_load['Nodes']:
                    if "pos" not in node:
                        graph.add_node(node["id"])
                    else:
                        pos = eval(str(node["pos"]))
                        graph.add_node(node["id"], pos)
                for edge in json_load['Edges']:
                    graph.add_edge(edge["src"], edge["dest"], edge["w"])
                self.graph = graph
                return True
        except Exception as exception:
            raise NotImplementedError
        finally:
            json_file.close()

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open('../data/' + file_name, "w") as write_file:
                json_graph = {"Edges": [], "Nodes": []}
                # save edges as json
                for id1 in self.get_graph().get_all_v().keys():
                    for id2, w in self.get_graph().all_out_edges_of_node(id1).items():
                        json_graph["Edges"].append({"src": id1, "dest": id2, "w": w})
                # save nodes as json
                for n in self.get_graph().get_all_v().values():
                    if n.location is None:
                        json_graph["Nodes"].append({"id": n.key})
                    else:
                        json_graph["Nodes"].append({"pos": str(n.location)[1: -1], "id": n.key})
                # json.dump(json_graph, write_file)
                json_output = json.dumps(json_graph, allow_nan=True, indent=len(json_graph))
                write_file.write(json_output)
            return True
        except Exception as e:
            raise NotImplementedError
        finally:
            write_file.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        keys = self.graph.get_all_v().keys()
        if id1 not in keys or id2 not in keys:
            return float('inf'), []

        if id1 == id2:
            return 0, []

        return self.dijkstra(id1, id2)

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass

    def dijkstra(self, src: int, dest: int) -> (float, list):
        # Set the distance to zero for our initial node
        # and to infinity for other nodes.
        distances = {node: math.inf for node in self.graph.get_all_v()}
        distances[src] = 0
        # Set a dictionary with the previous node of each node in the path
        # and set the previous node of the source node to inf key (which not one of the nodes in the graph)
        previous_nodes = {src: math.inf}
        # Set a heap queue and insert the source node
        q = []
        heapq.heappush(q, (0, src))

        while q:
            # Select the unvisited node with the smallest distance,
            # it's current node now.
            curr_node = heapq.heappop(q)[1]
            # Stop, if the smallest distance among the unvisited nodes is infinity.
            if distances[curr_node] == math.inf:
                break
            # Find unvisited neighbors for the current node
            # and calculate their distances through the current node.
            edges = self.graph.all_out_edges_of_node(curr_node)
            for neighbour in edges.keys():
                alternative_route = distances[curr_node] + edges.get(neighbour)
                # Compare the newly calculated distance to the assigned and save the smaller one.
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_nodes[neighbour] = curr_node
                    # Mark the current node as visited and push it the visited heap queue.
                    heapq.heappush(q, (distances[neighbour], neighbour))
                # If we have reached the destination node we done.
                if curr_node == dest:
                    break
        # There is no path
        if distances[dest] == math.inf:
            return float('inf'), []

        path, curr_node = [], dest
        while curr_node != src:
            path.insert(0, curr_node)  # append to left
            curr_node = previous_nodes[curr_node]
        if path:
            path.insert(0, curr_node)
        return distances[dest], path

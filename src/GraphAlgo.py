import heapq as hq
import json
import math
from typing import List
import sys

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

        return self.dijkstraAlgo(id1, id2)

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass

    """This is the Dijkstra's Algorithm implementation."""
    def dijkstraAlgo(self, src: int, dest: int) -> (float, list):
        # initializing the dist.
        # dist[src] is going to be zero and the rest inf.
        inf = sys.maxsize
        dist = {node: inf for node in self.graph.get_all_v()}
        dist[src] = 0
        # initializing a dictionary with the previous node of each node in the path and set the previous node of the source node to inf
        prev_nodes = {src: inf}
        # initializing a heap queue and insert the source node
        q = []
        hq.heappush(q, (0, src))  # hq = heap queue

        while q:
            # Step 1: find the unvisited node with the smallest distance, first iteration starts at current node.
            curr_node = hq.heappop(q)[1]

            # Condition 1: If the smallest distance among the unvisited nodes is infinity, then break.
            if dist[curr_node] == inf:
                break

            # loop through the unvisited nodes and calculate their distance from the src node.
            edges = self.graph.all_out_edges_of_node(curr_node)
            for neighbor in edges.keys():
                new_path = dist[curr_node] + edges.get(neighbor)
                # if the new_path is smaller than the current one, update..
                if new_path < dist[neighbor]:
                    dist[neighbor] = new_path
                    prev_nodes[neighbor] = curr_node
                    # Mark the current node as visited, insert it in the hq.
                    hq.heappush(q, (dist[neighbor], neighbor))
                # Condition 2: If the dest node is reached, break.
                if curr_node == dest:
                    break
        # Condition 3: If there is no path from src to dest:
        if dist[dest] == inf:
            return float('inf'), []
        # Creating the path list
        path = []
        curr_node = dest
        while curr_node != src:
            path.insert(0, curr_node)
            curr_node = prev_nodes[curr_node]
        if path:
            path.insert(0, curr_node)
        return dist[dest] / 1.0, path

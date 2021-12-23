import heapq as hq
import json
import math
from random import uniform
from typing import List
import sys
from matplotlib import pyplot as plt
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
            with open(file_name, "w") as write_file:
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
        temp = []  # temp node list
        if len(node_lst) == 0:  # check if the node's list is empty
            return None
        currNode = node_lst[0]
        temp.append(currNode)
        visitedNodes = []
        while len(node_lst) != 0:  # while there are still unvisited cities
            visitedNodes.append(currNode)  # add the current node to visitedNode list
            min_distance = sys.maxsize
            node_lst.remove(currNode)
            path = []  # init ans list of nodes
            for node in node_lst:  # go all over the unvisited nodes, calculate the closest one
                if node not in visitedNodes:
                    curr_distance = self.shortest_path(currNode, node)[0]
                    if curr_distance < min_distance:
                        min_distance = curr_distance
                        path = self.shortest_path(currNode, node)[1]  # add the closest node to path list
            for node in path:  # The closest node's path (out of all cities) is appended to the list which is to be returned
                if node is not path[0]:
                    temp.append(node)
                    visitedNodes.append(node)
                    node_lst.remove(node)
        if len(temp) == 0:
            return None
        distance = 0
        for i in range(len(temp)-1):
            distance += self.shortest_path(temp[i].key, temp[i+1].key)
        return temp, distance

    def centerPoint(self) -> (int, float):
        min_distance = math.inf
        node_id = 0
        curr_max = 0
        for Node1 in self.get_graph().get_all_v().values():
            for Node2 in self.get_graph().get_all_v().values():
                distance = self.shortest_path(Node1.key, Node2.key)[0]
                if distance > curr_max:
                    curr_max = distance
            if curr_max < min_distance:
                min_distance = curr_max
                node_id = Node1.key
            curr_max = 0
        ans = (node_id, min_distance)
        return ans

    def plot_graph(self) -> None:
        for node in self.get_graph().get_all_v().values():
            x, y, z = node.location
            plt.plot(x, y, markersize=30, marker='.', color='red')
            plt.text(x, y, str(node.key), color='black', fontsize=10)
            for dest_id, w in self.graph.all_out_edges_of_node(node.key).items():
                dest = self.graph.node_map.get(dest_id)
                x2, y2, z2 = dest.location
                plt.annotate("", xy=(x, y), xytext=(x2, y2), arrowprops=dict(arrowstyle="<-"))
                # mid_x = (x+x2)/2
                # mid_y = (y+y2)/2
                # plt.text(mid_x, mid_y, str(w)[0:4], color='black', fontsize=10)
        plt.show()


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

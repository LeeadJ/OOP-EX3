import json
from typing import List

from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import *


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph):
        self._graph = graph

    def get_graph(self) -> GraphInterface:
        return self._graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            json_load = json.load(file_name)
            for node in json_load['Nodes']:
                self.get_graph().add_node(node['id'], node['pos'])
            for edge in json_load['Edges']:
                self.get_graph().add_edge(edge['src'], edge['w'], edge['dest'])
            return True
        except:
            raise NotImplementedError

    def save_to_json(self, file_name: str) -> bool:
        list_json = ["Nodes"]
        list_edges = ["Edges"]
        for i in self.get_graph().get_all_v().keys():
            temp_dict = {}
            temp_dict['pos'] = self.get_graph().get_all_v().get(i).location
            temp_dict['id'] = self.get_graph().get_all_v().get(i).key
            list_json.append(temp_dict)
            for j in self.get_graph().all_out_edges_of_node(i):
                edge_dict = {}
                edge_dict['src'] = j.Src
                edge_dict['w'] = j.Weight
                edge_dict['dest'] = j.Dest
                list_edges.append(edge_dict)
        final_dict = {list_json, list_edges}
        with open('output.json', 'w') as fout:
            json.dump(final_dict, fout)
        return True

        # json_object = json.dumps(dictionary, indent=4)
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass

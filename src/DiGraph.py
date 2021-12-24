from src.GraphInterface import GraphInterface
from src.Edge import *
from src.Gnode import *


class DiGraph(GraphInterface):

    def __init__(self):
        self.node_map = {}
        self.edge_map = {}
        self.mc = 0

    def v_size(self) -> int:
        return len(self.node_map)

    def e_size(self) -> int:
        counter = 0
        for key in self.edge_map:
            counter += len(self.edge_map[key].values())
        return counter

    def get_all_v(self) -> dict:
        return self.node_map

    def all_in_edges_of_node(self, id1: int) -> dict:
        in_edges = {}
        try:
            for key in self.edge_map:
                for i in self.edge_map[key].values():
                    if i.Dest == id1:
                        in_edges[i.Src] = i.Weight
        except Exception as e:
            pass
        finally:
            return in_edges

    def all_out_edges_of_node(self, id1: int) -> dict:
        out_edges = {}
        try:
            for i in self.edge_map[id1].values():
                out_edges[i.Dest] = i.Weight
        except Exception as e:
            pass
        finally:
            return out_edges

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        #  create temp edge
        temp_edge = Edge(id1, weight, id2)
        #  check if node exits if not return flase
        if self.node_map.get(id1) is None or self.node_map.get(id2) is None:
            return False
        #  check if this edge has a dict if not create one and add the edge to it
        if self.edge_map.get(id1) is None:
            self.edge_map[id1] = {}
            self.edge_map[id1][id2] = temp_edge
            self.mc += 1
            return True
        # check if they key inside the dict exists
        elif self.edge_map.get(id1).get(id2) is None:
            self.edge_map[id1][id2] = temp_edge
            self.mc += 1
            return True
        # if this edge is already in the dict then do nothing
        else:
            print("could not connect edge")
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        temp_node = Gnode(node_id, pos)
        if self.node_map.get(node_id) is None:
            self.node_map[node_id] = temp_node
            self.mc += 1
            return True
        else:
            print("Could not add node {}".format(node_id))
            return False

    def remove_node(self, node_id: int) -> bool:
        if self.node_map.get(node_id) is None:
            print("Node {} doesn't exist ".format(node_id))
            return False
        else:
            self.node_map.pop(node_id)
            self.mc += 1
            return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.edge_map.get(node_id1).get(node_id2) is None:
            print("Edge doesn't exist")
            return False
        else:
            self.edge_map.get(node_id1).pop(node_id2)
            self.mc += 1
            return True

    def __repr__(self):
        return '|V|=%s , |E|=%s' % (self.v_size(), self.e_size())



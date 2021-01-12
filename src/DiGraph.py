from abc import ABC
from src.src.NodeData import NodeData
from src.src.GraphInterface import GraphInterface


class DiGraph(GraphInterface, ABC):
    def __init__(self, **kwargs):
        self._graph = dict()
        self._edge_dest = dict()
        self._edge_src = dict()
        self._size_of_edges = 0
        self._mc = 0

    def __repr__(self):
        return 'Nodes(x=%s)' % self._graph.keys()

    """
            Returns the number of vertices in this graph
    """

    def v_size(self) -> int:
        return len(self._graph.values())

    """
                Returns the number of edges in this graph
    """

    def e_size(self) -> int:
        return self._size_of_edges

    """
                return a dictionary of all the nodes in the Graph (the graph dictionary)
    """

    def get_all_v(self) -> dict:
        return self._graph

    """return a dictionary of all the nodes connected to (into) node_id (node id is the dest return the the 
    "dest_dict" that contains dictionaries- and Returns the dictionary that belongs to the node id that centers all 
    the edges and vertices that connect to it """

    def all_in_edges_of_node(self, id1: int) -> dict:
        if self._graph is not None:
            if self._graph.get(id1) is not None:
                return self._edge_dest[id1]

    """return a dictionary of all the nodes that node id connect to them (node id is the src) (return the the 
    "src_dict" that contains dictionaries- and Returns the dictionary that belongs to the node id that centers all 
    the edges and vertices that he connect to them """

    def all_out_edges_of_node(self, id1: int) -> dict:
        if self._graph is not None:
            if self._graph.get(id1) is not None:
                return self._edge_src[id1]

    """
                Returns the current version of this graph
    """

    def get_mc(self) -> int:
        return self._mc

    """id1: The start node of the edge id2: The end node of the edgeweight: The weight of the edge True if the edge 
    was added successfully False o.w.This action creates a edge between two vertices and determines a positive weigh 
    """

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        # check about contains func
        if self._graph is not None:
            if self._graph.get(id1) is not None and self._graph.get(id2) is not None and weight >= 0:
                if not self._edge_src.get(id1).__contains__(id2) \
                        and not self._edge_dest.get(id2).__contains__(id1):
                    self._edge_src[id1][id2] = weight
                    self._edge_dest[id2][id1] = weight
                    self._mc += 1
                    self._size_of_edges += 1
                    return True
                else:
                    self._edge_src[id1][id2] = weight
                    self._edge_dest[id2][id1] = weight
                    self._mc += 1
                    # check about the mc if old_weight==new_weight
                    return True
        return False

    """Adds a node to the graph.node_id: The node ID pos: The position of the nodeTrue if the node was added 
    successfully, False o.w.This action creates a node in the graph, by adding a new NodeData to the graph 
    dictionary and after we create the node we create is src and dest dictionaries inside src and dict dictionaries 
    Respectively """

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self._graph.get(node_id) is None:
            self._graph[node_id] = NodeData(key=node_id, pos=pos)
            self._edge_src[node_id] = dict()
            self._edge_dest[node_id] = dict()
            self._mc += 1
            return True
        return False

    """Removes a node from the graph. node_id: The node ID True if the node was removed successfully, 
    False o.w.remove the node from the graph and remove all the edges that connect to him and update the src_dest 
    dictionaries in accordance """

    def remove_node(self, node_id: int) -> bool:
        if not self._graph.get(node_id) is None:
            count = 0
            if self._edge_src.__contains__(node_id):
                del self._edge_src[node_id]
            src_list = []
            for key_src in self._edge_src.keys():
                src_list.append(key_src)
            for key_src in src_list:
                if self._edge_src.get(key_src).__contains__(node_id):
                    count += 1
                    del self._edge_src[key_src][node_id]
            if self._edge_dest.__contains__(node_id):
                del self._edge_dest[node_id]
            dest_list = []
            for key_dest in self._edge_dest.keys():
                dest_list.append(key_dest)
            for key_dest in dest_list:
                if self._edge_dest.get(key_dest).__contains__(node_id):
                    count += 1
                    del self._edge_dest[key_dest][node_id]
            self._size_of_edges = self._size_of_edges - count
            del self._graph[node_id]
            return True
        return False

    """Removes an edge from the graph. node_id1: The start node of the edge node_id2: The end node of the edgeTrue if 
    the edge was removed successfully, False o.w remove a edge from the graph and update node1 and node2 src and dest 
    dictionaries. """

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self._graph.get(node_id1) is not None and self._graph.get(node_id2) is not None \
                and self._edge_src.get(node_id1).__contains__(node_id2) \
                and self._edge_dest.get(node_id2).__contains__(node_id1):
            del self._edge_src[node_id1][node_id2]
            del self._edge_dest[node_id2][node_id1]
            self._size_of_edges -= 1
            return True
        return False

    """
         return the NodeData According to his node id this function will help us in plot function in GraphAlgo
    """

    def get_node(self, node_id) -> NodeData:
        return self._graph.get(node_id)

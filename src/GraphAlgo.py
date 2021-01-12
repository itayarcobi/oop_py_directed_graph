import heapq
import matplotlib.pyplot as plt
import json
from abc import ABC
import random

from src.src.GraphAlgoInterface import GraphAlgoInterface
from src.src.DiGraph import DiGraph
from src.src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface, ABC):
    def __init__(self, gr: DiGraph = None):
        if gr is None:
            self.graph = DiGraph()
        else:
            self.graph = gr
        self.qp = heapq

    """
           return the directed graph on which the algorithm works on
       """

    def get_graph(self) -> GraphInterface:
        return self.graph

    """
        Loads a graph from a json file.
        file_name: The path to the json file
        True if the loading was successful, False o.w.
        load and open json file According to the specific format we received in the data folder
        so we can work and use the loaded graph
        """

    def load_from_json(self, file_name: str) -> bool:
        gl = DiGraph()
        try:
            with open(file_name, "r") as file:
                my_dict = json.load(file)
                my_node = my_dict["Nodes"]
                my_edges = my_dict["Edges"]
                for i in range(len(my_node)):
                    j = my_node[i]
                    id = j["id"]
                    pos = None
                    if j.get("pos") is not None:
                        pos = j["pos"]
                    gl.add_node(id, pos)
                for i in range(len(my_edges)):
                    j = my_edges[i]
                    src = j["src"]
                    w = j["w"]
                    dest = j["dest"]
                    gl.add_edge(src, dest, w)
                    self.graph = gl
                return True
        except IOError as e:
            print(e)
            return False

    """Saves the graph in JSON format to a file file_name: The path to the out file True if the save was successful, 
    False o.w. save to json file According to the specific format we received in the data folder """

    def save_to_json(self, file_name: str, ) -> bool:
        save_dict = dict()
        Nodes = []
        Edges = []
        for i in self.graph.get_all_v().values():
            id = i.get_key()
            pos = i.get_pos()
            n = {"pos": pos, "id": id}
            Nodes.append(n)
        for i in self.graph.get_all_v().keys():
            for w, d in self.graph.all_out_edges_of_node(i).items():
                n0 = {"src": i, "w": d, "dest": w}
                Edges.append(n0)
        save_dict["Edges"] = Edges
        save_dict["Nodes"] = Nodes
        try:
            with open(file_name, "w") as file:
                json.dump(save_dict, default=lambda n: n.__dict__, indent=4, fp=file)
                return True
        except IOError as e:
            print(e)
            return False

    """Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm id1: The start node id id2: The 
    end node id Return The distance of the path, a list of the nodes ids that the path goes through In this function 
    we find the shortest trajectory between two vertices in a graph. 
    """

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        for keys in self.get_graph().get_all_v().values():
            keys.set_weight(float('inf'))
        nodes = self.get_graph().get_all_v()
        if nodes.get(id1) is None or nodes.get(id2) is None:
            return float('inf'), []
        nodes[id1].set_weight(0)
        heap = []
        heapq.heappush(heap, (nodes[id1].get_weight(), nodes[id1]))
        while len(heap) != 0:
            curr_node = heapq.heappop(heap)[1]
            for key, w in self.get_graph().all_out_edges_of_node(curr_node.get_key()).items():
                if nodes[key].get_weight() > w + curr_node.get_weight():
                    nodes[key].set_weight(w + curr_node.get_weight())
                    heapq.heappush(heap, (nodes[key].get_weight(), nodes[key]))
        curr_node = nodes[id2]
        if curr_node.get_weight() == float('inf'):
            return float('inf'), []
        list = [curr_node.get_key()]
        ans = curr_node.get_weight()
        while curr_node.get_weight() != 0:
            for key, w in self.get_graph().all_in_edges_of_node(curr_node.get_key()).items():
                if nodes[key].get_weight() + w == curr_node.get_weight():
                    list.insert(0, key)
                    curr_node = nodes[key]
        return ans, list

    """Finds the Strongly Connected Component(SCC) that node id1 is a part of. id1: The node id Return The list of 
    nodes in the SCC We find the binding element of a particular vertex.A binding component is all the vertices I can 
    reach and they too can reach me. 
    """

    def connected_component(self, id1: int) -> list:
        nodes = self.get_graph().get_all_v()
        for keys, t in nodes.items():
            nodes[keys].set_tag(-1)
        if nodes.get(id1) is None:
            return []
        nodes[id1].set_tag(0)
        list = [id1]
        list2 = [id1]
        while len(list) != 0:
            curr = list.pop(0)
            for key in self.get_graph().all_out_edges_of_node(curr).keys():
                if nodes[key].get_tag() == -1:
                    nodes[key].set_tag(0)
                    list.append(key)
                    list2.append(key)

        for keys, t in nodes.items():
            nodes[keys].set_tag(-1)

        list3 = [id1]
        list4 = [id1]
        while len(list3) != 0:
            curr2 = list3.pop(0)
            for key3 in self.get_graph().all_in_edges_of_node(curr2).keys():
                if nodes[key3].get_tag() == -1:
                    nodes[key3].set_tag(0)
                    list3.append(key3)
                    list4.append(key3)
        list5 = []
        for index2 in list2:
            for index4 in list4:
                if index2 == index4:
                    list5.append(index4)
                    break

        return sorted(list5)

    """
        Finds all the Strongly Connected Component(SCC) in the graph.
        Return The list all SCC
        We will perform connected_component on the whole graph.
        """

    def connected_components(self) -> list:
        nodes = self.get_graph().get_all_v()
        list2 = []
        nodes_keys = list(nodes.keys())
        while len(nodes_keys) != 0:
            curr = nodes_keys.pop(0)
            list_scc = self.connected_component(curr)
            list2.append(list_scc)
            for key in list_scc:
                for key_in in nodes_keys:
                    if key == key_in:
                        nodes_keys.remove(key_in)
        return list2

    """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner this function uses matplotlib functions
    """

    def plot_graph(self) -> None:
        node_lis = []
        x_lis = []
        y_lis = []
        counter = 0
        for npn in self.graph.get_all_v().values():
            if npn.get_pos() is None:
                counter += 1
                node_lis.append(npn)
            else:
                x_lis.append(npn.get_pos()[0])
                y_lis.append(npn.get_pos()[1])
        if counter == len(self.graph.get_all_v()):
            self.set_plot_loc(x_min=35, x_max=36, y_min=35, y_max=36, node_lis=node_lis)
        elif len(node_lis) > 0:
            x_max = -float('inf')
            x_min = float('inf')
            y_max = -float('inf')
            y_min = float('inf')
            for x in x_lis:
                if not isinstance(x, int):
                    if x.get_pos()[0] < x_min:
                        x_min = x.get_pos()[0]
                    elif x.get_pos()[0] > x_max:
                        x_max = x.get_pos()[0]
                # else:
                #     if x < x_min:
                #         x_min = x
                #     elif x > x_max:
                #         x_max = x
            for y in y_lis:
                if not isinstance(y, int):
                    if y.get_pos()[1] < y_min:
                        y_min = y.get_pos()[0]
                    elif y.get_pos()[1] > y_max:
                        y_max = y.get_pos()[1]
                # else:
                #     if y < y_min:
                #         y_min = y
                #     elif y > y_max:
                #         y_max = y

            self.set_plot_loc(x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max, node_lis=node_lis)

        fig, ax = plt.subplots()
        x_lis = []
        y_lis = []
        for i in self.graph.get_all_v().values():
            np = i.get_pos()
            ax.scatter(np[0], np[1], color="r", zorder=10)
            # ax.annotate(i.get_key(), np[0], np[1])
        for src in self.graph.get_all_v():
            for dest in self.graph.all_out_edges_of_node(src):
                x1 = self.graph.get_node(src).get_pos()[0]
                x2 = self.graph.get_node(dest).get_pos()[0]
                y1 = self.graph.get_node(src).get_pos()[1]
                y2 = self.graph.get_node(dest).get_pos()[1]
                plt.plot([x1, x2], [y1, y2])

        plt.xlabel("x axis ")
        plt.ylabel("y axis ")
        plt.title("OOP EX3")
        plt.show()

        pass

    def set_plot_loc(self, x_min, x_max, y_min, y_max, node_lis):

        for node in node_lis:
            rand_x = (random.random() * (x_max - x_min)) + x_min + 0.000001
            rand_y = (random.random() * (y_max - y_min)) + y_min + 0.000001
            print(rand_y)
            node.set_pos((rand_x, rand_y, 0))

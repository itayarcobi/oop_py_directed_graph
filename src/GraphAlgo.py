import heapq
import matplotlib.pyplot as plt
import json
from abc import ABC

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


    def get_graph(self) -> GraphInterface:
        return self.graph

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
                    pos=None
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
                json.dump(save_dict, default=lambda n: n._dict_, indent=4, fp=file)
                return True
        except IOError as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        for keys in self.get_graph().get_all_v().values():
            keys.set_weight(float('inf'))
        nodes = self.get_graph().get_all_v()
        if nodes.get(id1) is None or nodes.get(id2) is None:
            return float('inf'),[]
        nodes[id1].set_weight(0)
        heap = []
        heapq.heappush(heap, (nodes[id1].get_weight(), nodes[id1]))
        while len(heap) != 0:
            curr_node = heapq.heappop(heap)[1]
            for key, w in self.get_graph().all_out_edges_of_node(curr_node.get_key()).items():
                if nodes[key].get_weight() > w + curr_node.get_weight():
                    nodes[key].set_weight(w + curr_node.get_weight())
                    heapq.heappush(heap, (nodes[key].get_weight(),nodes[key]))
        curr_node = nodes[id2]
        if curr_node.get_weight() == float('inf'):
            return float('inf'), []
        list = [curr_node.get_key()]
        ans = curr_node.get_weight()
        while curr_node.get_weight() != 0:
            for key, w in self.get_graph().all_in_edges_of_node(curr_node.get_key()).items():
                if nodes[key].get_weight() + w == curr_node.get_weight():
                    list.insert(0,key)
                    curr_node = nodes[key]
        return ans, list

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

    def plot_graph(self) -> None:
        fig, ax = plt.subplots()
        for i in self.graph.get_all_v().values():
            np = i.get_pos()
            nid = i.get_key()
            # plt.plot(x[0], x[1], "o")
            ax.scatter(np[0], np[1])
            ax.annotate(nid, (np[0], np[1]))
            # for ed in self._g0.all_out_edges_of_node(i):
            plt.plot(np[0], np[1])

        plt.xlabel("x axis ")
        plt.ylabel("y axis ")
        plt.title("OOP EX3")
        plt.show()

        pass
    #
    # def regraph(self) -> GraphInterface:
    #     g1 = DiGraph()
    #     for i in self._g0.get_all_v():
    #         g1.add_node(i)
    #     print(g1)
    #     return g1

from unittest import TestCase

from src.src.DiGraph import DiGraph
from src.src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    def setUp(self):
        self.g = DiGraph()
        for n in range(10):
            self.g.add_node(n, (n, n))
        self.g.add_edge(0, 1, 1)
        self.g.add_edge(1, 0, 10)
        self.g.add_edge(1, 2, 1.2)
        self.g.add_edge(2, 3, 2.3)
        self.g.add_edge(1, 3, 1.3)
        self.g.add_edge(5, 3, 5.3)
        self.g.add_edge(1, 9, 1.9)
        self.g.add_edge(6, 7, 6.7)
        self.g.add_edge(4, 3, 4.3)
        self.g.add_edge(9, 0, 90)

        self.g0 = GraphAlgo(self.g)
        self.g0.get_graph()

    def test_get_graph(self):
        self.fail()

    def test_load_from_json(self):
        self.g0.load_from_json("graph.json")

    def test_save_to_json(self):
        self.g0.save_to_json("graph.json")

    def test_shortest_path(self):
        self.fail()

    def test_connected_component(self):
        self.fail()

    def test_connected_components(self):
        self.fail()

    def test_plot_graph(self):
        self.g0.plot_graph()

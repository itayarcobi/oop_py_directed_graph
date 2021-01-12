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
        self.g.add_edge(5, 3, 5.3)
        self.g.add_edge(1, 9, 1.9)
        self.g.add_edge(6, 7, 6.7)
        self.g.add_edge(1, 3, 1.3)
        self.g.add_edge(4, 3, 4.3)
        self.g.add_edge(4, 1, 0.4)
        self.g.add_edge(9, 0, 90)

        self.g0 = GraphAlgo(self.g)
        self.g0.get_graph()

    def test_save_load_from_json(self):
        self.g0.save_to_json("graph.json")
        gl = DiGraph()
        gl = self.g0.load_from_json("graph.json")
        self.assertTrue(self.g.__eq__(gl))

    def test_shortest_path(self):
        self.assertEqual(self.g0.shortest_path(0, 1)[0], 1)
        self.assertEqual(self.g0.shortest_path(0, 2)[0], 2.2)

    def test_connected_component(self):
        self.assertEqual(len(self.g0.connected_component(1)), 3)
        self.g.add_edge(3, 1, 31)
        self.assertEqual(len(self.g0.connected_component(1)), 5)
        self.g.remove_edge(9, 0)
        self.assertEqual(len(self.g0.connected_component(1)), 4)
        self.g.remove_node(1)
        self.assertFalse(len(self.g0.connected_component(1)))
        self.g.add_node(15)
        self.assertEqual(self.g0.connected_component(15), [15])
        self.g.add_node(16)
        self.g.add_edge(15, 16, 156)
        self.assertEqual(self.g0.connected_component(15), [15])
        self.g.add_edge(16, 15, 5)
        self.assertEqual(self.g0.connected_component(15), [15, 16])

    def test_connected_components(self):
        self.assertEqual(len(self.g0.connected_components()), 8)
        self.g.add_edge(3, 2, 3.2)
        self.assertEqual(len(self.g0.connected_components()), 7)
        self.g.remove_node(4)
        self.assertEqual(len(self.g0.connected_components()), 6)
        self.g.add_edge(5, 6, 56)
        self.g.add_edge(6, 7, 67)
        self.g.add_edge(7, 8, 87)
        self.g.add_edge(8, 5, 85)
        self.assertEqual(len(self.g0.connected_components()), 3)
        self.assertEqual(self.g0.connected_components(), [[0, 1, 9], [2, 3], [5, 6, 7, 8]])
        self.g.add_edge(9, 2, 92)
        self.g.add_edge(3, 0, 30)
        self.g.add_edge(1, 6, 16)
        self.g.add_edge(7, 9, 79)
        self.assertEqual(len(self.g0.connected_components()), 1)

    def test_plot_graph(self):
        self.g.add_node(10, (0, 4))
        self.g.add_node(15, (1, 7))
        self.g.add_edge(10, 15, 30)
        self.g0.plot_graph()

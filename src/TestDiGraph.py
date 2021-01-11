from unittest import TestCase

from src.src.DiGraph import DiGraph


class TestDiGraph(TestCase):

    def setUp(self):
        self.g = DiGraph()
        for n in range(10):
            self.g.add_node(n)
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

    def test_v_size(self):
        self.assertEqual(self.g.v_size(), 10)
        self.g.add_node(10)
        self.assertEqual(self.g.v_size(), 11)
        self.g.add_node(10)
        self.assertEqual(self.g.v_size(), 11)

    def test_e_size(self):
        self.assertEqual(self.g.e_size(), 10)
        self.g.add_edge(9, 5, 9.5)
        self.assertEqual(self.g.e_size(), 11)
        self.g.add_edge(9, 5, 6.8)
        self.assertEqual(self.g.e_size(), 11)
        self.g.add_edge(5, 9, 5.9)
        self.assertEqual(self.g.e_size(), 12)

    def test_get_all_v(self):
        self.assertEqual(len(self.g.get_all_v()), 10)
        self.g.add_node(10)
        self.assertEqual(len(self.g.get_all_v()), 11)

    def test_all_in_edges_of_node(self):
        self.assertEqual(len(self.g.all_in_edges_of_node(0)), 2)
        self.g.add_edge(5, 0, 50)
        self.assertEqual(len(self.g.all_in_edges_of_node(0)), 3)
        self.g.add_edge(5, 0, 5.5)
        self.assertEqual(len(self.g.all_in_edges_of_node(0)), 3)

    def test_all_out_edges_of_node(self):
        self.assertEqual(len(self.g.all_out_edges_of_node(1)), 4)
        self.g.add_edge(1, 7, 1.7)
        self.assertEqual(len(self.g.all_out_edges_of_node(1)), 5)
        self.g.add_edge(1, 7, 7.1)
        self.assertEqual(len(self.g.all_out_edges_of_node(1)), 5)

    def test_get_mc(self):
        self.assertEqual(self.g.get_mc(), 20)
        self.g.add_node(10)
        self.assertEqual(self.g.get_mc(), 21)
        self.g.add_edge(10, 5, 10.5)
        self.assertEqual(self.g.get_mc(), 22)

    def test_add_edge(self):
        self.assertEqual(self.g.e_size(), 10)
        self.assertFalse(self.g.add_edge(10, 1, 101))
        self.g.add_edge(5, 9, 59)
        self.assertEqual(self.g.e_size(), 11)
        self.g.add_edge(5, 9, 5.9)
        self.assertEqual(self.g.e_size(), 11)
        self.assertFalse(self.g.add_edge(11, 9, 5))
        self.assertFalse(self.g.add_edge(3, 1, -5))

    def test_add_node(self):
        self.assertEqual(len(self.g.get_all_v()), 10)
        self.g.add_node(10)
        self.assertEqual(len(self.g.get_all_v()), 11)
        self.g.add_node(10)
        self.assertEqual(len(self.g.get_all_v()), 11)

    def test_remove_node(self):
        self.assertEqual(len(self.g.get_all_v()), 10)
        self.g.add_node(10)
        self.g.add_node(11)
        self.g.add_node(12)
        self.g.add_edge(10, 11, 110)
        self.g.add_edge(10, 12, 112)
        self.g.add_edge(11, 12, 122)
        self.g.add_edge(12, 10, 1112)
        self.assertEqual(len(self.g.all_out_edges_of_node(10)), 2)
        self.assertEqual(len(self.g.all_in_edges_of_node(10)), 1)
        self.assertEqual(len(self.g.all_in_edges_of_node(12)), 2)
        self.g.remove_node(10)
        self.assertEqual(self.g.v_size(), 12)
        self.assertEqual(len(self.g.all_in_edges_of_node(12)), 1)
        self.assertEqual(len(self.g.all_out_edges_of_node(12)), 0)
        self.assertIsNone(self.g.all_out_edges_of_node(10))
        self.assertEqual(len(self.g.all_in_edges_of_node(11)), 0)
        self.assertEqual(self.g.e_size(), 11)

    def test_remove_edge(self):
        self.assertEqual(self.g.e_size(), 10)
        self.g.add_node(10)
        self.g.add_edge(10, 1, 101)
        self.assertEqual(self.g.e_size(), 11)
        self.assertEqual(len(self.g.all_in_edges_of_node(1)), 2)
        self.g.remove_edge(10, 1)
        self.assertEqual(self.g.e_size(), 10)
        self.assertEqual(len(self.g.all_out_edges_of_node(10)), 0)
        self.assertEqual(len(self.g.all_in_edges_of_node(1)), 1)

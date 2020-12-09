#!/usr/bin/env python3
##
# This module contains a reference implementation of an undirected graph data structure implemented
# using a vertex-indexed array of adjacency lists.
#
# V vertices are identified by the integers [0..V-1].
# Each edge appears twice in the data structure.
##

import unittest


class Graph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.num_edges = 0
        self.adj = [[] for _ in range(num_vertices)]

    def __str__(self):
        out = f"{self.num_vertices} vertices, {self.num_edges} edges\n"
        for v in range(self.num_vertices):
            out += f"{v}: {self.adjacent(v)}\n"
        return out

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.num_edges += 1

    def adjacent(self, v):
        return self.adj[v]

    def degree(self, v):
        return len(self.adjacent(v))

    def max_degree(self):
        maxval = 0
        for v in range(self.num_vertices):
            if self.degree(v) > maxval:
                maxval = self.degree(v)
        return maxval

    def avg_degree(self):
        return 2 * self.num_edges / self.num_vertices

    def num_self_loops(self):
        count = 0
        for v in range(self.num_vertices):
            for w in self.adjacent(v):
                if v == w:
                    count += 1
        return count / 2


def unconnected_graph():
    g = Graph(13)

    g.add_edge(0, 5)
    g.add_edge(4, 3)
    g.add_edge(0, 1)
    g.add_edge(6, 4)
    g.add_edge(5, 4)
    g.add_edge(0, 2)
    g.add_edge(0, 6)
    g.add_edge(5, 3)

    g.add_edge(7, 8)

    g.add_edge(9, 11)
    g.add_edge(9, 10)
    g.add_edge(9, 12)
    g.add_edge(11, 12)

    return g


def connected_graph():
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    return g


class TestGraph(unittest.TestCase):

    def test_unconnected_graph(self):
        g = unconnected_graph()
        self.assertEqual(g.num_vertices, 13)
        self.assertEqual(g.num_edges, 13)
        self.assertEqual(g.degree(0), 4)
        self.assertEqual(g.degree(1), 1)
        self.assertEqual(g.degree(3), 2)
        self.assertEqual(g.degree(9), 3)
        self.assertEqual(g.max_degree(), 4)

    def test_connected_graph(self):
        g = connected_graph()
        self.assertEqual(g.num_vertices, 6)
        self.assertEqual(g.num_edges, 8)
        self.assertEqual(g.degree(0), 3)
        self.assertEqual(g.degree(1), 2)
        self.assertEqual(g.degree(2), 4)
        self.assertEqual(g.degree(3), 3)
        self.assertEqual(g.max_degree(), 4)


if __name__ == "__main__":
    unittest.main()


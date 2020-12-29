#!/usr/bin/env python3
##
# Depth-first search.
##

import unittest
import graph


class RecursiveDFS:

    def __init__(self, graph, source_vertex):
        self.num_vertices = graph.num_vertices
        self.marked = [False for _ in range(graph.num_vertices)]
        self.count = 0
        self._dfs(graph, source_vertex)

    def _dfs(self, graph, v):
        self.marked[v] = True
        self.count += 1
        for w in graph.adjacent(v):
            if not self.marked[w]:
                self._dfs(graph, w)

    def is_marked(self, w):
        return self.marked[w]

    def is_connected(self):
        return self.count == self.num_vertices


class StackBasedDFS:

    def __init__(self, graph, source_vertex):
        self.num_vertices = graph.num_vertices
        self.marked = [False for _ in range(graph.num_vertices)]

        stack = [source_vertex]
        self.marked[source_vertex] = True
        self.count = 1

        while stack:
            v = stack.pop()
            for w in graph.adjacent(v):
                if not self.marked[w]:
                    stack.append(w)
                    self.marked[w] = True
                    self.count += 1

    def is_marked(self, w):
        return self.marked[w]

    def is_connected(self):
        return self.count == self.num_vertices


class TestDFS(unittest.TestCase):

    def test_recursive_dfs_unconnected(self):
        g = graph.unconnected_graph()
        dfs = RecursiveDFS(g, 0)
        self.assertEqual(dfs.count, 7)
        self.assertEqual(dfs.is_marked(1), True)
        self.assertEqual(dfs.is_marked(6), True)
        self.assertEqual(dfs.is_marked(5), True)
        self.assertEqual(dfs.is_marked(7), False)
        self.assertEqual(dfs.is_marked(9), False)
        self.assertEqual(dfs.is_connected(), False)

    def test_recursive_dfs_connected(self):
        g = graph.connected_graph()
        dfs = RecursiveDFS(g, 0)
        self.assertEqual(dfs.is_connected(), True)

    def test_stack_dfs_unconnected(self):
        g = graph.unconnected_graph()
        dfs = StackBasedDFS(g, 0)
        self.assertEqual(dfs.count, 7)
        self.assertEqual(dfs.is_marked(1), True)
        self.assertEqual(dfs.is_marked(6), True)
        self.assertEqual(dfs.is_marked(5), True)
        self.assertEqual(dfs.is_marked(7), False)
        self.assertEqual(dfs.is_marked(9), False)
        self.assertEqual(dfs.is_connected(), False)

    def test_stack_dfs_connected(self):
        g = graph.connected_graph()
        dfs = StackBasedDFS(g, 0)
        self.assertEqual(dfs.is_connected(), True)


if __name__ == "__main__":
    unittest.main()


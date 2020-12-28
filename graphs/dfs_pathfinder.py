#!/usr/bin/env python3
##
# This module uses depth-first search to find paths in a graph.
##

import graph


class DepthFirstPathfinder:

    def __init__(self, graph, source_vertex):
        self.marked = [False for _ in range(graph.num_vertices)]
        self.edge_to = [None for _ in range(graph.num_vertices)]
        self.source_vertex = source_vertex
        self._dfs(graph, source_vertex)

    def _dfs(self, graph, v):
        self.marked[v] = True
        for w in graph.adjacent(v):
            if not self.marked[w]:
                self.edge_to[w] = v
                self._dfs(graph, w)

    def has_path_to(self, v):
        return self.marked[v]

    def get_path_to(self, v):
        path = []
        if self.has_path_to(v):
            target = v
            while target != self.source_vertex:
                path.append(target)
                target = self.edge_to[target]
            path.append(self.source_vertex)
            path.reverse()
        return path


def test_graph():
    g = graph.Graph(6)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    return g


if __name__ == "__main__":
    g = test_graph()
    paths = DepthFirstPathfinder(g, 0)
    print(paths.get_path_to(5))


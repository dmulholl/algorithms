#!/usr/bin/env python3
##
# This module uses depth-first search to identify the connected components in an undirected graph.
##

import graph


class ConnectedComponents:

    def __init__(self, graph):
        self.marked = [False for _ in range(graph.num_vertices)]
        self.component_ids = [None for _ in range(graph.num_vertices)]
        self.component_count = 0

        for source_vertex in range(graph.num_vertices):
            if not self.marked[source_vertex]:
                self._dfs(graph, source_vertex)
                self.component_count += 1

    def _dfs(self, graph, v):
        self.marked[v] = True
        self.component_ids[v] = self.component_count
        for w in graph.adjacent(v):
            if not self.marked[w]:
                self._dfs(graph, w)

    def connected(self, v, w):
        return self.component_ids[v] == self.component_ids[w]

    def component_id(self, v):
        return self.component_ids[v]


def make_graph():
    g = graph.Graph(13)

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


def main():
    g = make_graph()
    cc = ConnectedComponents(g)

    components = {i: [] for i in range(cc.component_count)}

    for v in range(g.num_vertices):
        components[cc.component_id(v)].append(v)

    for i in range(cc.component_count):
        print(f"{i}: {components[i]}")


if __name__ == "__main__":
    main()

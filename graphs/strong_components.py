#!/usr/bin/env python3
##
# This module uses Kosaraju's algorithm to determine the strongly-connected components in a
# directed graph. (Vertices are 'strongly connected' if they are mutually reachable.)
##

import digraph


class StronglyConnectedComponents:

    def __init__(self, digraph):
        self.marked = [False for _ in range(digraph.num_vertices)]
        self.component_ids = [None for _ in range(digraph.num_vertices)]
        self.component_count = 0

        order = DepthFirstOrder(digraph.reverse())

        for source_vertex in order.reverse_postorder():
            if not self.marked[source_vertex]:
                self._dfs(digraph, source_vertex)
                self.component_count += 1

    def _dfs(self, digraph, v):
        self.marked[v] = True
        self.component_ids[v] = self.component_count
        for w in digraph.adjacent(v):
            if not self.marked[w]:
                self._dfs(digraph, w)

    def strongly_connected(self, v, w):
        return self.component_ids[v] == self.component_ids[w]

    def component_id(self, v):
        return self.component_ids[v]


class DepthFirstOrder:

    def __init__(self, digraph):
        self.preorder = []
        self.postorder = []
        self.marked = [False for _ in range(digraph.num_vertices)]

        for v in range(digraph.num_vertices):
            if not self.marked[v]:
                self._dfs(digraph, v)

    def _dfs(self, digraph, v):
        self.preorder.append(v)
        self.marked[v] = True
        for w in digraph.adjacent(v):
            if not self.marked[w]:
                self._dfs(digraph, w)
        self.postorder.append(v)

    def reverse_postorder(self):
        return list(reversed(self.postorder))


def make_graph():
    g = digraph.Digraph(13)

    g.add_edge(0, 5)
    g.add_edge(0, 1)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 2)
    g.add_edge(3, 5)
    g.add_edge(4, 2)
    g.add_edge(4, 3)
    g.add_edge(5, 4)
    g.add_edge(6, 0)
    g.add_edge(6, 4)
    g.add_edge(6, 9)
    g.add_edge(7, 6)
    g.add_edge(7, 8)
    g.add_edge(8, 7)
    g.add_edge(8, 9)
    g.add_edge(9, 10)
    g.add_edge(9, 11)
    g.add_edge(10, 12)
    g.add_edge(11, 4)
    g.add_edge(11, 12)
    g.add_edge(12, 9)

    return g


def main():
    g = make_graph()
    scc = StronglyConnectedComponents(g)

    components = {i: [] for i in range(scc.component_count)}

    for v in range(g.num_vertices):
        components[scc.component_id(v)].append(v)

    for i in range(scc.component_count):
        print(f"{i}: {components[i]}")


if __name__ == "__main__":
    main()

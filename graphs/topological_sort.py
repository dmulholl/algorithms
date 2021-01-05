#!/usr/bin/env python3
##
# Topological sort: the vertices of a digraph are ordered such that all directed edges point from
# a vertex earlier in the order to a vertex later in the order.
#
# A digraph has a topological order IFF it is a DAG.
##

import digraph
import cycle_detector


class TopologicalSort:

    def __init__(self, digraph):
        self.order = None
        self.is_dag = not cycle_detector.CycleDetector(digraph).has_cycle()
        if self.is_dag:
            dfo = DepthFirstOrder(digraph)
            self.order = list(reversed(dfo.postorder))


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


def make_dag():
    d = digraph.Digraph(13)
    d.add_edge(0, 1)
    d.add_edge(0, 5)
    d.add_edge(0, 6)
    d.add_edge(2, 0)
    d.add_edge(2, 3)
    d.add_edge(3, 5)
    d.add_edge(5, 4)
    d.add_edge(6, 4)
    d.add_edge(6, 9)
    d.add_edge(7, 6)
    d.add_edge(8, 7)
    d.add_edge(9, 10)
    d.add_edge(9, 11)
    d.add_edge(9, 12)
    d.add_edge(11, 12)
    return d


def main():
    top_sort = TopologicalSort(make_dag())
    print(top_sort.order)


if __name__ == "__main__":
    main()

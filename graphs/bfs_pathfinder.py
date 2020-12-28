#!/usr/bin/env python3
##
# This module uses breadth-first search to find the shortest (i.e. minimum number of hops) paths
# in a graph.
##

import graph


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


class BreadthFirstPathfinder:

    def __init__(self, graph, source_vertex):
        self.marked = [False for _ in range(graph.num_vertices)]
        self.edge_to = [None for _ in range(graph.num_vertices)]
        self.source_vertex = source_vertex

        queue = Queue()
        self.marked[source_vertex] = True
        queue.enqueue(source_vertex)

        while not queue.is_empty():
            v = queue.dequeue()
            for w in graph.adjacent(v):
                if not self.marked[w]:
                    self.edge_to[w] = v
                    self.marked[w] = True
                    queue.enqueue(w)

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
    g.add_edge(0, 1)
    g.add_edge(0, 5)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(3, 4)
    return g


if __name__ == "__main__":
    g = test_graph()
    paths = BreadthFirstPathfinder(g, 0)
    print(paths.get_path_to(3))


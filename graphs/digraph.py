##
# This module contains a reference implementation of a directed graph implemented using a
# vertex-indexed array of adjacency lists.
#
# V vertices are identified by the integers [0..V-1].
##

class Digraph:

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
        self.num_edges += 1

    def adjacent(self, v):
        return self.adj[v]

    def reverse(self):
        new_digraph = Digraph(self.num_vertices)
        for v in range(self.num_vertices):
            for w in self.adj[v]:
                new_digraph.add_edge(w, v)
        return new_digraph


#!/usr/bin/env python3
##
# This module detects cycles in directed graphs. A directed graph without cycles is called a DAG,
# a directed acyclic graph.
##

import digraph


class CycleDetector:

    def __init__(self, digraph):
        self.marked = [False for _ in range(digraph.num_vertices)]
        self.on_stack = [False for _ in range(digraph.num_vertices)]
        self.edge_to = [None for _ in range(digraph.num_vertices)]
        self.cycle = []

        for v in range(digraph.num_vertices):
            if not self.marked[v]:
                self._dfs(digraph, v)

    def _dfs(self, digraph, v):
        self.on_stack[v] = True
        self.marked[v] = True
        for w in digraph.adjacent(v):
            if self.has_cycle():
                return
            elif not self.marked[w]:
                self.edge_to[w] = v
                self._dfs(digraph, w)
            elif self.on_stack[w]:
                current = v
                while current != w:
                    self.cycle.append(current)
                    current = self.edge_to[current]
                self.cycle.append(w)
                self.cycle.append(v)
                self.cycle.reverse()
        self.on_stack[v] = False

    def has_cycle(self):
        return len(self.cycle) != 0


def make_digraph():
    d = digraph.Digraph(6)
    d.add_edge(0, 1)
    d.add_edge(0, 2)
    d.add_edge(0, 5)
    d.add_edge(5, 4)
    d.add_edge(4, 3)
    d.add_edge(3, 5)
    return d


def main():
    d = make_digraph()
    cd = CycleDetector(d)
    print(f"Has Cycle: {cd.has_cycle()}")
    print(f"Cycle: {cd.cycle}")


if __name__ == "__main__":
    main()

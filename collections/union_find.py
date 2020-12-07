#!/usr/bin/env python3
##
# This module contains a reference implementation of a union-find (aka disjoint-set) data
# structure. This structure uses a 'forest-of-trees' representation to store a collection of
# disjoint sets.
#
# Sedgewick, R. and Wayne, K. (2011) Algorithms. 4th Edition. Addison-Wesley, p.216.
##

import unittest


class UnionFind:

    # Initialize a new collection containing `n` integer elements and `count` sets.
    def __init__(self, n):
        self.ids = [i for i in range(n)]
        self.sizes = [1 for i in range(n)]
        self.count = n

    # Returns true if elements `p` and `q` are in the same set.
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    # Returns the integer ID of the set containing element `p`.
    def find(self, p):
        while p != self.ids[p]:
            p = self.ids[p]
        return p

    # Merge the set containing element `p` with the set containing element `q`.
    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return

        # Point the smaller root to the larger one.
        if self.sizes[p_root] < self.sizes[q_root]:
            self.ids[p_root] = q_root
            self.sizes[q_root] += self.sizes[p_root]
        else:
            self.ids[q_root] = p_root
            self.sizes[p_root] += self.sizes[q_root]
        self.count -= 1


class TestUnionFind(unittest.TestCase):

    connected_pairs = [
        (4, 3),
        (3, 8),
        (6, 5),
        (9, 4),
        (2, 1),
        (5, 0),
        (7, 2),
        (6, 1),
    ]

    def test_unionfind(self):
        uf = UnionFind(10)
        for p, q in self.connected_pairs:
           uf.union(p, q)
        self.assertTrue(uf.connected(0, 0))
        self.assertTrue(uf.connected(0, 1))
        self.assertTrue(uf.connected(0, 2))
        self.assertTrue(uf.connected(0, 5))
        self.assertTrue(uf.connected(0, 6))
        self.assertTrue(uf.connected(0, 7))
        self.assertFalse(uf.connected(0, 3))
        self.assertFalse(uf.connected(0, 4))
        self.assertTrue(uf.connected(3, 4))
        self.assertTrue(uf.connected(8, 9))
        self.assertTrue(uf.connected(3, 9))


if __name__ == '__main__':
    unittest.main()


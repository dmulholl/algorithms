#!/usr/bin/env python3
##
# This module contains a reference implementation of a hash-based symbol table implemented as an
# array of linked lists.
##

import unittest
from seq_search_table import SeqSearchTable


class SeparateChainingHashTable:

    def __init__(self, m=997):
        self.n = 0 # Number of entries.
        self.m = m # Hash table array size.
        self.table = [SeqSearchTable() for _ in range(m)]

    # Returns the number of entries.
    def size(self):
        return self.n

    # Returns an integer in the inclusive range [0..m].
    def hash(self, key):
        return hash(key) % self.m

    # Returns the value paired with `key` if a corresponding entry is found, otherwise None.
    def get(self, key):
        return self.table[self.hash(key)].get(key)

    # Inserts a key-value pair into the table. Will overwrite the existing value if `key` is
    # already present in the table.
    def set(self, key, value):
        self.n += self.table[self.hash(key)].set(key, value)

    # Returns true if the table contains an entry for `key`.
    def contains(self, key):
        return self.table[self.hash(key)].contains(key)

    # Deletes the entry for `key` from the table.
    def delete(self, key):
        seq_table = self.table[self.hash(key)]
        old_size = seq_table.size
        seq_table.delete(key)
        if seq_table.size != old_size:
            self.n -= 1


class TestSeparateChainingHashTable(unittest.TestCase):

    def test_symbol_table(self):
        ht = SeparateChainingHashTable()
        ht.set("a", 123)
        ht.set("b", 456)
        ht.set("c", 789)
        self.assertEqual(ht.size(), 3)
        self.assertEqual(ht.contains("a"), True)
        self.assertEqual(ht.contains("z"), False)
        self.assertEqual(ht.get("a"), 123)
        self.assertEqual(ht.get("b"), 456)
        self.assertEqual(ht.get("c"), 789)
        ht.delete("a")
        ht.delete("c")
        self.assertEqual(ht.size(), 1)
        self.assertEqual(ht.contains("a"), False)
        self.assertEqual(ht.get("b"), 456)


if __name__ == '__main__':
    unittest.main()

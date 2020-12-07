#!/usr/bin/env python3
##
# Hash table with separate chaining.
#
# This module contains a reference implementation of a hash-based symbol table implemented as an
# array of linked lists.
#
# Ideally the array size m should always be a prime number. (Can implement using a table of the
# smallest primes greater than each power of two.)
##

import unittest
from symbol_table import SymbolTable


class SeparateChainingHashTable:

    def __init__(self, m=997):
        self.n = 0 # Number of entries.
        self.m = m # Hash table array size.
        self.table = [SymbolTable() for _ in range(m)]

    # Returns the number of key-value entries.
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
        self.n += self.table[self.hash(key)].delete(key)


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

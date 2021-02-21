#!/usr/bin/env python3
##
# Hash table with linear probing.
#
# This module contains a reference implementation of a hash-based symbol table implemented using
# linear probing.
#
# The load factor n/m needs to be less than 1/2 for satisfactory performance.

# Ideally the array size m should always be a prime number. (Can implement using a table of the
# smallest primes greater than each power of two.)
##

import unittest


class LinearProbingHashTable:

    def __init__(self, m=16):
        self.n = 0 # Number of key-value entries.
        self.m = m # Size of the linear-probing table.
        self.keys = [None for _ in range(m)]
        self.values = [None for _ in range(m)]

   # Returns the number of key-value entries.
    def size(self):
        return self.n

    # Resize the table. The load factor alpha = n/m should be between 1/2 and 1/8.
    def resize(self, new_size):
        temp = LinearProbingHashTable(new_size)
        for i in range(self.m):
            if self.keys[i] is not None:
                temp.set(self.keys[i], self.values[i])
        self.keys = temp.keys
        self.values = temp.values
        self.m = temp.m

    # Returns an integer in the range 0 to m - 1.
    def hash(self, key):
        return hash(key) % self.m

    # Returns the value paired with `key` if a corresponding entry is found, otherwise None.
    def get(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.m
        return None

    # Inserts a key-value pair into the table. Will overwrite the existing value if `key` is
    # already present in the table.
    def set(self, key, value):
        if self.n >= self.m // 2:
            self.resize(self.m * 2)

        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.m
        self.keys[index] = key
        self.values[index] = value
        self.n += 1

    # Returns true if the table contains an entry for `key`.
    def contains(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return True
            index = (index + 1) % self.m
        return False

    # Deletes the entry for `key` from the table.
    def delete(self, key):
        if not self.contains(key):
            return

        index = self.hash(key)
        while not key == self.keys[index]:
            index = (index + 1) % self.m
        self.keys[index] = None
        self.values[index] = None

        index = (index + 1) % self.m
        while self.keys[index] is not None:
            key_to_redo = self.keys[index]
            value_to_redo = self.values[index]
            self.keys[index] = None
            self.values[index] = None
            self.n -= 1
            self.set(key_to_redo, value_to_redo)
            index = (index + 1) % self.m

        self.n -= 1
        if self.n <= self.m // 8:
            self.resize(self.m // 2)


class TestLinearProbingHashTable(unittest.TestCase):

    def test_symbol_table(self):
        ht = LinearProbingHashTable()
        ht.set("a", 123)
        ht.set("z", 123)
        ht.set("b", 456)
        ht.set("p", 456)
        ht.set("c", 789)
        ht.set("q", 789)
        self.assertEqual(ht.size(), 6)
        self.assertEqual(ht.contains("a"), True)
        self.assertEqual(ht.contains("x"), False)
        self.assertEqual(ht.get("a"), 123)
        self.assertEqual(ht.get("b"), 456)
        self.assertEqual(ht.get("c"), 789)
        ht.delete("a")
        ht.delete("c")
        self.assertEqual(ht.size(), 4)
        self.assertEqual(ht.contains("a"), False)
        self.assertEqual(ht.get("b"), 456)


if __name__ == '__main__':
    unittest.main()

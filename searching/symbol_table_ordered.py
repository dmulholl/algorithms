#!/usr/bin/env python3
##
# This module contains a reference implementation of an ordered symbol table -- a data structure
# which stores key-value pairs sorted by key-order.
#
# This implementation uses a pair of parallel arrays, one for keys and one for values. This makes
# it too slow for real-world use with large datasets as both the insert and delete operations are
# O(n).
##

import unittest


class OrderedSymbolTable:

    def __init__(self, capacity):
        self.keys = [None for _ in range(capacity)]
        self.values = [None for _ in range(capacity)]
        self.size = 0

    def is_empty(self):
        return self.size == 0

    # Returns the value paired with `key` if a corresponding entry is found, otherwise None.
    def get(self, key):
        if self.is_empty():
            return None
        i = self.rank(key)
        if i < self.size and self.keys[i] == key:
            return self.values[i]
        else:
            return None

    # Inserts a key-value pair into the table. Will overwrite the existing value if `key` is
    # already present in the table.
    def set(self, key, value):
        i = self.rank(key)
        if i < self.size and self.keys[i] == key:
            self.values[i] = value
            return
        for j in range(self.size, i, -1):
            self.keys[j] = self.keys[j - 1]
            self.values[j] = self.values[j - 1]
        self.keys[i] = key
        self.values[i] = value
        self.size += 1

    # Deletes the entry for `key` from the table.
    def delete(self, key):
        i = self.rank(key)
        if i < self.size and self.keys[i] == key:
            for j in range(i, self.size - 1):
                self.keys[j] = self.keys[j + 1]
                self.values[j] = self.values[j + 1]
            self.size -= 1

    # Returns true if the table contains an entry for `key`.
    def contains(self, key):
        i = self.rank(key)
        if i < self.size and self.keys[i] == key:
            return True
        return False

    # Returns the number of entries with a key less than `key`.
    def rank(self, key):
        low, high = 0, self.size - 1
        while low <= high:
            mid = low + (high - low) // 2
            if key < self.keys[mid]:
                high = mid - 1
            elif key > self.keys[mid]:
                low = mid + 1
            else:
                return mid
        return low

    # Returns the smallest key.
    def min(self):
        return self.keys[0]

    # Returns the largest key.
    def max(self):
        return self.keys[self.size - 1]

    # Returns the largest key less than or equal to `key`.
    def floor(self, key):
        i = rank(key)
        if i < self.size and self.keys[i] == key:
            return key
        if i > 0:
            return self.keys[i - 1]
        else:
            return None

    # Returns the smallest key greater than or equal to `key`.
    def ceiling(self, key):
        i = self.rank(key)
        if i < self.size:
            return self.keys[i]
        else:
            return None

    # Returns the key of rank `k`.
    def select(self, k):
        return self.keys[k]

    # Deletes the entry with the smallest key.
    def delete_min(self):
        self.delete(self.min())

    # Deletes the entry with the largest key.
    def delete_max(self):
        self.delete(self.max())

    # Returns the number of entries with keys in the inclusive interval [low..high].
    def count(self, low, high):
        if high < low:
            return 0
        elif self.contains(high):
            return self.rank(high) - self.rank(low) + 1
        else:
            return self.rank(high) - self.rank(low)

    # Returns a list of keys in the inclusive interval [low..high] in sorted order.
    def keys_in_range(self, low, high):
        keys = []
        for i in range(self.rank(low), self.rank(high)):
            keys.append(self.keys[i])
        if self.contains(high):
            keys.append(self.keys[self.rank(high)])
        return keys

    # Returns a list of all keys in sorted order.
    def all_keys(self):
        return self.keys_in_range(self.min(), self.max())


class TestOrderedSymbolTable(unittest.TestCase):

    def test_symbol_table(self):
        ost = OrderedSymbolTable(capacity=10)
        ost.set("e", 1)
        ost.set("a", 2)
        ost.set("m", 3)
        ost.set("i", 4)
        ost.set("d", 5)

        self.assertEqual(ost.size, 5)
        self.assertEqual(ost.get("e"), 1)
        self.assertEqual(ost.get("m"), 3)
        self.assertEqual(ost.get("d"), 5)
        self.assertEqual(ost.contains("e"), True)
        self.assertEqual(ost.contains("z"), False)
        self.assertEqual(ost.all_keys(), ["a", "d", "e", "i", "m"])

        ost.delete_max()
        ost.delete_min()
        ost.delete("e")
        self.assertEqual(ost.all_keys(), ["d", "i"])


if __name__ == '__main__':
    unittest.main()

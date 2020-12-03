#!/usr/bin/env python3
##
# This module contains a reference implementation of a symbol table data structure (aka a map,
# dictionary, associative array), implemented using a linked list with sequential search.
##

import unittest


class Node:

    def __init__(self, key, value, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node


class SeqSearchTable:

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    # Returns the value paired with `key` if a corresponding entry is found, otherwise None.
    def get(self, key):
        node = self.head
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    # Inserts a key-value pair into the table. Will overwrite the existing value if `key` is
    # already present in the table. (Returns 1 if it adds a new entry, 0 if it overwrites an
    # existing extry.)
    def set(self, key, value):
        node = self.head
        while node is not None:
            if node.key == key:
                node.value = value
                return 0
            node = node.next
        self.head = Node(key, value, self.head)
        self.size += 1
        return 1

    # Deletes the entry for `key` from the table.
    def delete(self, key):
        if self.is_empty():
            return
        elif self.head.key == key:
            self.head = self.head.next
            self.size -= 1
        else:
            node = self.head
            while node.next is not None:
                if node.next.key == key:
                    node.next = node.next.next
                    self.size -= 1
                    break
                node = node.next

    # Returns true if the table contains an entry for `key`.
    def contains(self, key):
        node = self.head
        while node is not None:
            if node.key == key:
                return True
            node = node.next
        return False


class TestSeqSearchTable(unittest.TestCase):

    def test_symbol_table(self):
        st = SeqSearchTable()
        st.set("a", 123)
        st.set("b", 456)
        st.set("c", 789)
        self.assertEqual(st.size, 3)
        self.assertEqual(st.contains("a"), True)
        self.assertEqual(st.get("a"), 123)
        self.assertEqual(st.get("b"), 456)
        self.assertEqual(st.get("c"), 789)
        st.delete("a")
        st.delete("c")
        self.assertEqual(st.size, 1)
        self.assertEqual(st.contains("a"), False)
        self.assertEqual(st.get("b"), 456)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
##
# This module contains a reference implementation for a linked list collection type.
##

import unittest


class Node:

    def __init__(self, item=None):
        self.item = item
        self.next = None


class Iterator:

    def __init__(self, first_node):
        self.next_node = first_node

    def __next__(self):
        if self.next_node is not None:
            node = self.next_node
            self.next_node = node.next
            return node.item
        raise StopIteration


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        return str(list(self))

    def __iter__(self):
        return Iterator(self.head)

    # O(n): Returns a copy of the list.
    def copy(self):
        new_list = LinkedList()
        node = self.head
        while node is not None:
            new_list.append(node.item)
            node = node.next
        return new_list

    # O(n): Returns the node at the specified index (0 < index < list.size).
    def get_node_at_index(self, index):
        if index < 0 or index >= self.size:
            raise Exception(f"index ({index}) out of bounds")
        node = self.head
        while index > 0:
            node = node.next
            index -= 1
        return node

    # O(1): Adds an item to the end of the list.
    def append(self, item):
        new_node = Node(item)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    # O(1): Adds an item to the start of the list.
    def prepend(self, item):
        new_node = Node(item)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    # O(n): Inserts an item into the list at the specified index (0 < index <= list.size).
    def insert(self, index, item):
        if index < 0 or index > self.size:
            raise Exception(f"index ({index}) out of bounds")
        if index == 0:
            self.prepend(item)
        elif index < self.size:
            preceding_node = self.get_node_at_index(index - 1)
            new_node = Node(item)
            new_node.next = preceding_node.next
            preceding_node.next = new_node
            self.size += 1
        else:
            self.append(item)

    # O(1): Removes and returns the first node from the list.
    def remove_first_node(self):
        if self.size == 0:
            raise Exception("list is empty")
        elif self.size == 1:
            node = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return node
        else:
            node = self.head
            self.head = self.head.next
            self.size -= 1
            return node

    # O(n): Removes and returns the last node from the list.
    def remove_last_node(self):
        if self.size == 0:
            raise Exception("list is empty")
        elif self.size == 1:
            node = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return node
        else:
            node = self.tail
            self.tail = self.get_node_at_index(self.size - 2)
            self.tail.next = None
            self.size -= 1
            return node

    # O(n): Reverses the list in-place.
    def reverse(self):
        new_list = LinkedList()
        while self.size > 0:
            new_list.prepend(self.remove_first_node().item)
        self.head = new_list.head
        self.tail = new_list.tail
        self.size = new_list.size

    # O(n): Returns true if the list contains an item equal to the specified item.
    def contains(self, item):
        node = self.head
        while node is not None:
            if node.item == item:
                return True
            node = node.next
        return False


class TestLinkedList(unittest.TestCase):

    def test_append(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        self.assertEqual(llist.size, 3)
        self.assertEqual(list(llist), [1, 2, 3])

    def test_prepend(self):
        llist = LinkedList()
        llist.prepend(1)
        llist.prepend(2)
        llist.prepend(3)
        self.assertEqual(llist.size, 3)
        self.assertEqual(list(llist), [3, 2, 1])

    def test_copy(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        copy = llist.copy()
        self.assertEqual(copy.size, 3)
        self.assertEqual(list(llist), [1, 2, 3])

    def test_get_node_at_index(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        self.assertEqual(llist.get_node_at_index(0).item, 1)
        self.assertEqual(llist.get_node_at_index(1).item, 2)
        self.assertEqual(llist.get_node_at_index(2).item, 3)

    def test_insert(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.insert(0, 0)
        llist.insert(4, 4)
        llist.insert(4, 99)
        self.assertEqual(llist.size, 6)
        self.assertEqual(list(llist), [0, 1, 2, 3, 99, 4])

    def test_reverse(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.reverse()
        self.assertEqual(llist.size, 3)
        self.assertEqual(list(llist), [3, 2, 1])

    def test_remove_first_node(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.remove_first_node()
        self.assertEqual(list(llist), [2, 3])

    def test_remove_last_node(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.remove_last_node()
        self.assertEqual(list(llist), [1, 2])

    def test_contains(self):
        llist = LinkedList()
        self.assertEqual(llist.contains(123), False)
        llist.append(123)
        self.assertEqual(llist.contains(123), True)
        self.assertEqual(llist.contains(456), False)

    def test_iteration(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        self.assertEqual([item for item in llist], [1, 2, 3])


if __name__ == '__main__':
    unittest.main()


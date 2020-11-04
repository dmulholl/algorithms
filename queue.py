#!/usr/bin/env python3
##
# This module contains a reference implementation of a FIFO queue based on a linked list.
# To enqueue an item we add it to the end of the list, to dequeue an item we remove it from
# the front of the list.
##

import unittest


class Node:

    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        item = self.head.item
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return item


class TestQueue(unittest.TestCase):

    def test_queue(self):
        queue = Queue()
        self.assertEqual(queue.size, 0)
        self.assertEqual(queue.is_empty(), True)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.size, 3)
        self.assertEqual(queue.is_empty(), False)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.size, 2)


if __name__ == '__main__':
    unittest.main()


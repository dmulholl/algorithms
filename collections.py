#!/usr/bin/env python3
##
# This module contains reference implementations of a number of basic collection types.
##

import unittest


# A bag allows items to be collected and iterated over but not removed.
# Iteration order is unspecified.
class Bag:

    def __init__(self):
        self.items = []

    def __iter__(self):
        return iter(self.items)

    def add(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


# A queue is a first-in-first-out (FIFO) collection.
class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


# A stack is a last-in-first-out (LIFO) collection.
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


class TestCollections(unittest.TestCase):

    def test_bag(self):
        bag = Bag()
        bag.add(1)
        bag.add(2)
        bag.add(3)
        self.assertEqual(bag.size(), 3)
        self.assertEqual(bag.is_empty(), False)
        self.assertEqual([item for item in bag], [1, 2, 3])

    def test_queue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.is_empty(), False)
        self.assertEqual(queue.dequeue(), 1)

    def test_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.pop(), 3)


if __name__ == '__main__':
    unittest.main()


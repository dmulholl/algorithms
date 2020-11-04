#!/usr/bin/env python3
##
# This module contains a reference implementation of a LIFO stack based on a linked list.
# Items are pushed to and popped from the head of the list.
##

import unittest


class Node:

    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class Stack:

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self.head = Node(item, self.head)
        self.size += 1

    def pop(self):
        item = self.head.item
        self.head = self.head.next
        self.size -= 1
        return item


class TestStack(unittest.TestCase):

    def test_stack(self):
        stack = Stack()
        self.assertEqual(stack.size, 0)
        self.assertEqual(stack.is_empty(), True)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.size, 3)
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.size, 2)


if __name__ == '__main__':
    unittest.main()


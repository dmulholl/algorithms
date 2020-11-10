#!/usr/bin/env python3
##
# This module contains a reference implementation of a priority queue based on a binary heap.
##

import unittest
import random


# Base class for both max and min priority queues.
class PriorityQueue:

    def __init__(self, capacity):
        self.size = 0
        self.heap = [None for i in range(capacity + 1)]

    def is_empty(self):
        return self.size == 0

    # Inserts an item.
    def insert(self, item):
        self.size += 1
        self.heap[self.size] = item
        self._swim(self.size)

    # Removes and returns the top (max or min) item from the queue.
    def remove(self):
        item = self.heap[1]
        self._swap(1, self.size)
        self.heap[self.size] = None
        self.size -= 1
        self._sink(1)
        return item

    # Returns the top (max or min) item without removing it.
    def peek(self):
        return self.heap[1]

    # Swaps heap elements at indices `p` and `q`.
    def _swap(self, p, q):
        self.heap[p], self.heap[q] = self.heap[q], self.heap[p]


# Always returns the maximum item from the queue.
class MaxPriorityQueue(PriorityQueue):

    def _swim(self, i):
        while i > 1 and self.heap[i//2] < self.heap[i]:
            self._swap(i//2, i)
            i = i // 2

    def _sink(self, i):
        while 2 * i <= self.size:
            j = 2 * i
            if j < self.size and self.heap[j] < self.heap[j+1]:
                j = j + 1
            if self.heap[i] >= self.heap[j]:
                break
            self._swap(i, j)
            i = j


# Always returns the minimum item from the queue.
class MinPriorityQueue(PriorityQueue):

    def _swim(self, i):
        while i > 1 and self.heap[i//2] > self.heap[i]:
            self._swap(i//2, i)
            i = i // 2

    def _sink(self, i):
        while 2 * i <= self.size:
            j = 2 * i
            if j < self.size and self.heap[j] > self.heap[j+1]:
                j = j + 1
            if self.heap[i] < self.heap[j]:
                break
            self._swap(i, j)
            i = j


class TestPriorityQueue(unittest.TestCase):

    def test_max_pq_small(self):
        pq = MaxPriorityQueue(10)
        for value in [1, 7, 3, 5, 11, 9]:
            pq.insert(value)
        self.assertEqual(pq.size, 6)
        self.assertEqual(pq.remove(), 11)
        self.assertEqual(pq.remove(), 9)
        self.assertEqual(pq.remove(), 7)
        self.assertEqual(pq.remove(), 5)
        self.assertEqual(pq.remove(), 3)
        self.assertEqual(pq.remove(), 1)
        self.assertEqual(pq.size, 0)

    def test_max_pq_large(self):
        pq = MaxPriorityQueue(1000)
        values = [i for i in range(1000)]
        random.shuffle(values)
        for value in values:
            pq.insert(value)
        self.assertEqual(pq.size, 1000)
        self.assertEqual(pq.remove(), 999)
        self.assertEqual(pq.remove(), 998)
        self.assertEqual(pq.remove(), 997)
        self.assertEqual(pq.remove(), 996)
        self.assertEqual(pq.remove(), 995)
        self.assertEqual(pq.size, 995)

    def test_min_pq_small(self):
        pq = MinPriorityQueue(10)
        for value in [1, 7, 3, 5, 11, 9]:
            pq.insert(value)
        self.assertEqual(pq.size, 6)
        self.assertEqual(pq.remove(), 1)
        self.assertEqual(pq.remove(), 3)
        self.assertEqual(pq.remove(), 5)
        self.assertEqual(pq.remove(), 7)
        self.assertEqual(pq.remove(), 9)
        self.assertEqual(pq.remove(), 11)
        self.assertEqual(pq.size, 0)

    def test_min_pq_large(self):
        pq = MinPriorityQueue(1000)
        values = [i for i in range(1000)]
        random.shuffle(values)
        for value in values:
            pq.insert(value)
        self.assertEqual(pq.size, 1000)
        self.assertEqual(pq.remove(), 0)
        self.assertEqual(pq.remove(), 1)
        self.assertEqual(pq.remove(), 2)
        self.assertEqual(pq.remove(), 3)
        self.assertEqual(pq.remove(), 4)
        self.assertEqual(pq.size, 995)


if __name__ == '__main__':
    unittest.main()


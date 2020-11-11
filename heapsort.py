#!/usr/bin/env python3
##
# This module contains a reference implementation of the heapsort algorithm.
# Sedgewick, R. and Wayne, K. (2011) Algorithms. 4th Edition. Addison-Wesley, p.336.
##

import unittest
import random


def sort(array):
    n = len(array)

    # Heap construction.
    i = n // 2
    while i >= 1:
        sink(array, i, n)
        i -= 1

    # Sortdown.
    while n > 1:
        swap(array, 1, n)
        n -= 1
        sink(array, 1, n)


def sink(array, i, n):
    while 2 * i <= n:
        j = 2 * i
        if j < n and less(array, j, j + 1):
            j = j + 1
        if not less(array, i, j):
            break
        swap(array, i, j)
        i = j


def swap(array, p, q):
    p -= 1
    q -= 1
    array[p], array[q] = array[q], array[p]


def less(array, p, q):
    p -= 1
    q -= 1
    return array[p] < array[q]


# Returns true if the input is empty, of length 1, or sorted in ascending order.
def is_sorted(array):
    for index in range(1, len(array)):
        if array[index] < array[index - 1]:
            return False
    return True


class TestSort(unittest.TestCase):

    def test_sort(self):
        test_array = [i for i in range(1000)]
        while is_sorted(test_array):
            random.shuffle(test_array)
        sort(test_array)
        self.assertTrue(is_sorted(test_array))


if __name__ == '__main__':
    unittest.main()


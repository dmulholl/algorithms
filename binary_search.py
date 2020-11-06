#!/usr/bin/env python3
##
# This module contains a reference implementation of the binary search algorithm. This
# algorithm searches an input array (which must already be sorted in increasing order) for
# a target value. If the target is found its index is returned, otherwise -1 is returned.
##

import unittest


def binary_search(array, target):
    l_index, r_index = 0, len(array) - 1
    while l_index <= r_index:
        m_index = l_index + (r_index - l_index) // 2
        if array[m_index] < target:
            l_index = m_index + 1
        elif array[m_index] > target:
            r_index = m_index - 1
        else:
            return m_index
    return -1


def recursive_binary_search(array, l_index, r_index, target):
    if l_index <= r_index:
        m_index = l_index + (r_index - l_index) // 2
        if array[m_index] < target:
            return recursive_binary_search(array, m_index + 1, r_index, target)
        elif array[m_index] > target:
            return recursive_binary_search(array, l_index, m_index - 1, target)
        else:
            return m_index
    else:
        return -1


def rec_search(array, target):
    return recursive_binary_search(array, 0, len(array) - 1, target)


class TestBinarySearch(unittest.TestCase):

    test_array = [11, 22, 33, 44, 55, 66, 77, 88, 99]

    def test_recursive_found(self):
        self.assertEqual(rec_search(self.test_array, 11), 0)
        self.assertEqual(rec_search(self.test_array, 22), 1)
        self.assertEqual(rec_search(self.test_array, 55), 4)
        self.assertEqual(rec_search(self.test_array, 88), 7)
        self.assertEqual(rec_search(self.test_array, 99), 8)

    def test_recursive_not_found(self):
        self.assertEqual(rec_search(self.test_array, 10), -1)
        self.assertEqual(rec_search(self.test_array, 12), -1)
        self.assertEqual(rec_search(self.test_array, 54), -1)
        self.assertEqual(rec_search(self.test_array, 56), -1)
        self.assertEqual(rec_search(self.test_array, 98), -1)
        self.assertEqual(rec_search(self.test_array, 100), -1)

    def test_iterative_found(self):
        self.assertEqual(binary_search(self.test_array, 11), 0)
        self.assertEqual(binary_search(self.test_array, 22), 1)
        self.assertEqual(binary_search(self.test_array, 55), 4)
        self.assertEqual(binary_search(self.test_array, 88), 7)
        self.assertEqual(binary_search(self.test_array, 99), 8)

    def test_iterative_not_found(self):
        self.assertEqual(binary_search(self.test_array, 10), -1)
        self.assertEqual(binary_search(self.test_array, 12), -1)
        self.assertEqual(binary_search(self.test_array, 54), -1)
        self.assertEqual(binary_search(self.test_array, 56), -1)
        self.assertEqual(binary_search(self.test_array, 98), -1)
        self.assertEqual(binary_search(self.test_array, 100), -1)


if __name__ == '__main__':
    unittest.main()


#!/usr/bin/env python3
##
# This module contains a reference implementation of the selection sort algorithm.
##

import unittest
import random


def sort(array):
    for i in range(len(array)):
        index_of_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[index_of_min]:
                index_of_min = j
        array[i], array[index_of_min] = array[index_of_min], array[i]


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


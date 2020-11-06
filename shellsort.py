#!/usr/bin/env python3
##
# This module contains a reference implementation of the shellsort algorithm.
##

import unittest
import random


def shellsort(array):
    h = 1
    while h < len(array) // 3:
        h = h * 3 + 1

    while h >= 1:
        for i in range(h, len(array)):
            j = i
            while j >= h:
                if array[j - h] > array[j]:
                    array[j - h], array[j] = array[j], array[j - h]
                else:
                    break
                j -= h
        h = h // 3


# Returns true if the input is empty, of length 1, or sorted in ascending order.
def is_sorted(array):
    for index in range(1, len(array)):
        if array[index] < array[index - 1]:
            return False
    return True


class TestShellsort(unittest.TestCase):

    def test_shellsort(self):
        test_array = [i for i in range(1000)]
        while is_sorted(test_array):
            random.shuffle(test_array)
        shellsort(test_array)
        self.assertTrue(is_sorted(test_array))


if __name__ == '__main__':
    unittest.main()


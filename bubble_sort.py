#!/usr/bin/env python3
##
# This module contains a reference implementation of the bubble sort algorithm.
##

import unittest
import random


def bubble_sort(array):
    while True:
        swapped = False
        for index in range(1, len(array)):
            if array[index - 1] > array[index]:
                array[index - 1], array[index] = array[index], array[index - 1]
                swapped = True
        if not swapped:
            break


# Returns true if the input is empty, of length 1, or sorted in ascending order.
def is_sorted(array):
    for index in range(1, len(array)):
        if array[index] < array[index - 1]:
            return False
    return True


class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        test_array = [i for i in range(1000)]
        while is_sorted(test_array):
            random.shuffle(test_array)
        bubble_sort(test_array)
        self.assertTrue(is_sorted(test_array))


if __name__ == '__main__':
    unittest.main()


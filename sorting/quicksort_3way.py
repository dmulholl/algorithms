#!/usr/bin/env python3
##
# This module contains a reference implementation of the quicksort algorithm with 3-way
# partitioning. This algorithm is more efficient than standard quicksort for arrays with
# large numbers of duplicate elements.
##

import unittest
import random


def sort(array):
    random.shuffle(array)
    quicksort3(array, 0, len(array) - 1)


# Sorts the slice of `array` identified by the inclusive indices `l_index` and `r_index`.
def quicksort3(array, l_index, r_index):
    if r_index <= l_index:
        return

    lt = l_index
    gt = r_index
    i = l_index + 1
    pivot = array[l_index]

    while i <= gt:
        if array[i] < pivot:
            array[lt], array[i] = array[i], array[lt]
            lt += 1
            i += 1
        elif array[i] > pivot:
            array[i], array[gt] = array[gt], array[i]
            gt -= 1
        else:
            i += 1

    quicksort3(array, l_index, lt - 1)
    quicksort3(array, gt + 1, r_index)


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


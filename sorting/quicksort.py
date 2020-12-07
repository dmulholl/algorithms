#!/usr/bin/env python3
##
# This module contains a reference implementation of the quicksort algorithm.
##

import unittest
import random


def sort(array):
    random.shuffle(array)
    quicksort(array, 0, len(array) - 1)


# Sorts the slice of `array` identified by the inclusive indices `l_index` and `r_index`.
def quicksort(array, l_index, r_index):
    if l_index < r_index:
        p = partition(array, l_index, r_index)
        quicksort(array, l_index, p - 1)
        quicksort(array, p + 1, r_index)


# Partitions the slice of `array` identified by the inclusive indices `l_index` and `r_index`.
def partition(array, l_index, r_index):
    l, r = l_index, r_index + 1
    pivot = array[l_index]

    while True:
        while True:
            l += 1
            if array[l] >= pivot or l == r_index:
                break
        while True:
            r -= 1
            if array[r] <= pivot or r == l_index:
                break
        if l >= r:
            break
        array[l], array[r] =  array[r], array[l]

    array[l_index], array[r], = array[r], array[l_index]
    return r


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


#!/usr/bin/env python3
##
# This module contains a reference implementation of the top-down mergesort algorithm.
##

import unittest
import random


def mergesort(array):
    sort(array, array.copy(), 0, len(array) - 1)


# Sorts the slice of `array` identified by the inclusive indices `low` and `high`. The auxiliary
# array is used as scratch space and should have the same length as `array`.
def sort(array, aux_array, low, high):
    if high <= low:
        return
    mid = low + (high - low) // 2
    sort(array, aux_array, low, mid)
    sort(array, aux_array, mid + 1, high)
    merge(array, aux_array, low, mid, high)


# Performs an in-place merge of the sorted slices array[low..mid] and array[mid+1..high].
# (Indices are inclusive.)
def merge(array, aux_array, low, mid, high):
    i, j = low, mid + 1

    for k in range(low, high + 1):
        aux_array[k] = array[k]

    for k in range(low, high + 1):
        if i > mid:
            array[k] = aux_array[j]
            j += 1
        elif j > high:
            array[k] = aux_array[i]
            i += 1
        elif aux_array[i] < aux_array[j]:
            array[k] = aux_array[i]
            i += 1
        else:
            array[k] = aux_array[j]
            j += 1


# Returns true if the input is empty, of length 1, or sorted in ascending order.
def is_sorted(array):
    for index in range(1, len(array)):
        if array[index] < array[index - 1]:
            return False
    return True


class TestMergesort(unittest.TestCase):

    def test_mergesort(self):
        test_array = [i for i in range(1000)]
        while is_sorted(test_array):
            random.shuffle(test_array)
        mergesort(test_array)
        self.assertTrue(is_sorted(test_array))


if __name__ == '__main__':
    unittest.main()


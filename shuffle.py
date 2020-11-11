#!/usr/bin/env python3
##
# This module contains an implementation of the Fisher-Yates/Durstenfeld algorithm for randomly
# shuffling an array.
##

import unittest
import random


# O(n): iterate over the array and at each index choose randomly from the remaining unshuffled
# entries. (The loop skips the final index as a minor optimization to avoid swapping the last
# element with itself.)
def shuffle(array):
    for i in range(len(array) - 1):
        j = random.randrange(i, len(array))
        swap(array, i, j)


# This algorithm is often implemented using a backwards loop as in many languages this makes the
# math for selecting the random element nicer. (As above, the loop skips index zero as a minor
# optimization to avoid swapping the first element with itself.)
def backwards_shuffle(array):
    for i in range(len(array) - 1, 0, -1):
        j = random.randrange(i + 1)
        swap(array, i, j)


# Swap the array entries at indices `p` and `q`.
def swap(array, p, q):
    array[p], array[q] = array[q], array[p]


if __name__ == '__main__':
    array = [i for i in range(10)]
    print(array)
    shuffle(array)
    print(array)


#!/usr/bin/env python3

import sys
import time
import random

import bubble_sort
import insertion_sort
import selection_sort
import shellsort
import mergesort
import quicksort
import quicksort_3way
import heapsort


SMALL = 1_000
LARGE = 10_000


algorithms = [
    bubble_sort,
    selection_sort,
    insertion_sort,
    shellsort,
    mergesort,
    quicksort,
    quicksort_3way,
    heapsort,
]


def runtime(func, arg):
    start = time.perf_counter()
    func(arg)
    return time.perf_counter() - start


def shuffle(array):
    random.shuffle(array)
    return array


if "uni" in sys.argv or "uniform" in sys.argv:
    small_array = [1 for i in range(SMALL)]
    large_array = [1 for i in range(LARGE)]
elif "asc" in sys.argv or "ascending" in sys.argv:
    small_array = [i for i in range(SMALL)]
    large_array = [i for i in range(LARGE)]
elif "des" in sys.argv or "descending" in sys.argv:
    small_array = [i for i in range(SMALL, 0, -1)]
    large_array = [i for i in range(LARGE, 0, -1)]
elif "dup" in sys.argv or "duplicates" in sys.argv:
    small_array = [random.randint(0, 50) for i in range(SMALL)]
    large_array = [random.randint(0, 50) for i in range(LARGE)]
else:
    small_array = shuffle([i for i in range(SMALL)])
    large_array = shuffle([i for i in range(LARGE)])


for algorithm in algorithms:
    t_small = runtime(algorithm.sort, small_array.copy())
    t_large = runtime(algorithm.sort, large_array.copy())
    print(f"{algorithm.__name__:16} {t_small:12.4f} {t_large:12.4f}")


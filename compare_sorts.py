#!/usr/bin/env python3

import sys
import time
import random

import bubble_sort
import insertion_sort
import selection_sort
import shellsort
import mergesort


SMALL = 1_000
LARGE = 10_000


algorithms = [
    bubble_sort.bubble_sort,
    selection_sort.selection_sort,
    insertion_sort.insertion_sort,
    shellsort.shellsort,
    mergesort.mergesort,
]


def runtime(func, arg):
    start = time.perf_counter()
    func(arg)
    return time.perf_counter() - start


def shuffle(array):
    random.shuffle(array)
    return array


if "uniform" in sys.argv:
    small_array = [1 for i in range(SMALL)]
    large_array = [1 for i in range(LARGE)]
elif "ascending" in sys.argv:
    small_array = [i for i in range(SMALL)]
    large_array = [i for i in range(LARGE)]
elif "descending" in sys.argv:
    small_array = [i for i in range(SMALL, 0, -1)]
    large_array = [i for i in range(LARGE, 0, -1)]
else:
    small_array = shuffle([i for i in range(SMALL)])
    large_array = shuffle([i for i in range(LARGE)])


for algorithm in algorithms:
    t_small = runtime(algorithm, small_array.copy())
    t_large = runtime(algorithm, large_array.copy())
    print(f"{algorithm.__name__:16} {t_small:12.4f} {t_large:12.4f}")


#!/usr/bin/env python3
##
# This module contains algorithms for calculating the greatest common divisor (gcd) of two or more
# integers which are not all zero. The gcd is the largest positive integer that divides each of
# the integers in the set.
#
# Euclid's algorithm relies on the observation that the gcd of two numbers also divides their
# difference.
##

import unittest


# Euclid using division. Assumes p and q are non-negative and not both zero.
def euclid_1(p, q):
    if q == 0:
        return p
    return euclid_1(q, p % q)


# Euclid using subtraction. Assumes p and q are both positive integers.
def euclid_2(p, q):
    if p == q:
        return p
    elif p > q:
        return euclid_2(p - q, q)
    elif q > p:
        return euclid_2(p, q - p)


# Returns the gcd of a set of non-negative integers, not all zero.
def gcd_of_set(*args):
    gcd = args[0]
    for i in range(1, len(args)):
        gcd = euclid_1(gcd, args[i])
    return gcd


class TestGCD(unittest.TestCase):

    def test_euclid_1(self):
        self.assertEqual(euclid_1(5, 0), 5)
        self.assertEqual(euclid_1(0, 5), 5)
        self.assertEqual(euclid_1(5, 5), 5)
        self.assertEqual(euclid_1(1, 5), 1)
        self.assertEqual(euclid_1(5, 1), 1)
        self.assertEqual(euclid_1(10, 25), 5)
        self.assertEqual(euclid_1(25, 10), 5)
        self.assertEqual(euclid_1(651, 889), 7)

    def test_euclid_2(self):
        self.assertEqual(euclid_2(5, 5), 5)
        self.assertEqual(euclid_2(1, 5), 1)
        self.assertEqual(euclid_2(5, 1), 1)
        self.assertEqual(euclid_2(10, 25), 5)
        self.assertEqual(euclid_2(25, 10), 5)
        self.assertEqual(euclid_2(651, 889), 7)

    def test_gcd_of_set(self):
        self.assertEqual(gcd_of_set(10), 10)
        self.assertEqual(gcd_of_set(10, 15), 5)
        self.assertEqual(gcd_of_set(10, 15, 20, 25), 5)


if __name__ == '__main__':
    unittest.main()


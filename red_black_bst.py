#!/usr/bin/env python3
##
# This module contains a reference implementation of an ordered symbol table implemented using
# a red-black binary search tree (BST).
##

import unittest
import random


RED = True
BLACK = False


# Node.size contains the number of nodes in the subtree rooted at the Node instance.
class Node:

    def __init__(self, key, value, size, color):
        self.key = key
        self.value = value
        self.size = size
        self.left = None
        self.right = None
        self.color = color


# Null nodes are considered black.
def is_red(node):
    if node is None:
        return False
    return node.color == RED


# Rotate a right-leaning red link to lean to the left.
def rotate_left(node):
    x = node.right
    node.right = x.left
    x.left = node
    x.color = node.color
    node.color = RED
    x.size = node.size
    node.size = size(node.left) + size(node.right) + 1
    return x


# Rotate a left-leaning red link to lean to the right.
def rotate_right(node):
    x = node.left
    node.left = x.right
    x.right = node
    x.color = node.color
    node.color = RED
    x.size = node.size
    node.size = size(node.left) + size(node.right) + 1
    return x


# Insertion/deletion helper.
def flip_colors(node):
    node.color = not node.color
    node.left.color = not node.left.color
    node.right.color = not node.right.color


# Returns the size of the subtree rooted at `node`.
def size(node):
    return 0 if node is None else node.size


# Returns the value associated with `key` in the subtree rooted at `node`. Returns None if `key`
# is not found.
def get(node, key):
    if node is None:
        return None
    if key < node.key:
        return get(node.left, key)
    elif key > node.key:
        return get(node.right, key)
    else:
        return node.value


# If `key` is found in the subtree rooted at `node`, set it's value to `value`. Otherwise add a
# new node to the subtree for the key-value pair.
def set(node, key, value):
    if node is None:
        return Node(key, value, 1, RED)
    if key < node.key:
        node.left = set(node.left, key, value)
    elif key > node.key:
        node.right = set(node.right, key, value)
    else:
        node.value = value

    if is_red(node.right) and not is_red(node.left):
        node = rotate_left(node)
    if is_red(node.left) and is_red(node.left.left):
        node = rotate_right(node)
    if is_red(node.left) and is_red(node.right):
        flip_colors(node)

    node.size = size(node.left) + size(node.right) + 1
    return node


# Returns the node containing the smallest key.
def min(node):
    if node.left is None:
        return node
    return min(node.left)


# Returns the node containing the largest key.
def max(node):
    if node.right is None:
        return node
    return max(node.right)


# Returns the node with the largest key less than or equal to `key`.
def floor(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return floor(node.left, key)
    if (r_floor := floor(node.right, key)) is not None:
        return r_floor
    else:
        return node


# Returns the node with the smallest key greater than or equal to `key`.
def ceiling(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key > node.key:
        return ceiling(node.right, key)
    if (l_ceiling := ceiling(node.left, key)) is not None:
        return l_ceiling
    else:
        return node


# Returns the node containing the key of rank k.
def select(node, k):
    if node is None:
        return None
    l_size = size(node.left)
    if l_size > k:
        return select(node.left, k)
    elif l_size < k:
        return select(node.right, k - l_size - 1)
    else:
        return node


# Returns the number of keys less than `key` in the subtree rooted at `node`.
def rank(node, key):
    if node is None:
        return 0
    if key < node.key:
        return rank(node.left, key)
    elif key > node.key:
        return 1 + size(node.left) + rank(node.right, key)
    else:
        return size(node.left)


# Deletion helper.
def balance(node):
    if is_red(node.right):
        node = rotate_left(node)
    if is_red(node.right) and not is_red(node.left):
        node = rotate_left(node)
    if is_red(node.left) and is_red(node.left.left):
        node = rotate_right(node)
    if is_red(node.left) and is_red(node.right):
        flip_colors(node)
    node.size = size(node.left) + size(node.right) + 1
    return node


# Deletion helper.
def move_red_left(node):
    flip_colors(node)
    if is_red(node.right.left):
        node.right = rotate_right(node.right)
        node = rotate_left(node)
    return node


# Deletes the node with the smallest key.
def delete_min(node):
    if node.left is None:
        return None
    if not is_red(node.left) and not is_red(node.left.left):
        node = move_red_left(node)
    node.left = delete_min(node.left)
    return balance(node)


# Deletion helper.
def move_red_right(node):
    flip_colors(node)
    if not is_red(node.left.left):
        node = rotate_right(node)
    return node


# Deletes the node with the largest key.
def delete_max(node):
    if is_red(node.left):
        node = rotate_right(node)
    if node.right is None:
        return None
    if not is_red(node.right) and not is_red(node.right.left):
        node = move_red_right(node)
    node.right = delete_max(node.right)
    return balance(node)


# Deletes the node with the specified key.
def delete(node, key):
    if key < node.key:
        if not is_red(node.left) and not is_red(node.left.left):
            node = move_red_left(node)
        node.left = delete(node.left, key)
    else:
        if is_red(node.left):
            node = rotate_right(node)
        if key == node.key and node.right is None:
            return None
        if not is_red(node.right) and not is_red(node.right.left):
            node = move_red_right(node)
        if key == node.key:
            node.value = get(node.right, min(node.right).key)
            node.key = min(node.right).key
            node.right = delete_min(node.right)
        else:
            node.right = delete(node.right, key)
    return balance(node)


# Returns an ordered list of keys in the inclusive range [low..high].
# Pass an empty list as `keylist` on the first call.
def keys_in_range(node, keylist, low, high):
    if node is None:
        return
    if low < node.key:
        keys_in_range(node.left, keylist, low, high)
    if low <= node.key and node.key <= high:
        keylist.append(node.key)
    if high > node.key:
        keys_in_range(node.right, keylist, low, high)


# This wrapper class provides the public interface to the library.
class RedBlackBST:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return size(self.root)

    def get(self, key):
        return get(self.root, key)

    def set(self, key, value):
        self.root = set(self.root, key, value)
        self.root.color = BLACK

    def min(self):
        return min(self.root).key

    def max(self):
        return max(self.root).key

    def floor(self, key):
        node = floor(self.root, key)
        if node is None:
            return None
        return node.key

    def ceiling(self, key):
        node = ceiling(self.root, key)
        if node is None:
            return None
        return node.key

    def select(self, k):
        return select(self.root, k).key

    def rank(self, key):
        return rank(self.root, key)

    def delete_min(self):
        if not is_red(self.root.left) and not is_red(self.root.right):
            self.root.color = RED
        self.root = delete_min(self.root)
        if not self.is_empty():
            self.root.color = BLACK

    def delete_max(self):
        if not is_red(self.root.left) and not is_red(self.root.right):
            self.root.color = RED
        self.root = delete_max(self.root)
        if not self.is_empty():
            self.root.color = BLACK

    def delete(self, key):
        if not is_red(self.root.left) and not is_red(self.root.right):
            self.root.color = RED
        self.root = delete(self.root, key)
        if not self.is_empty():
            self.root.color = BLACK

    def keys_in_range(self, low, high):
        keylist = []
        keys_in_range(self.root, keylist, low, high)
        return keylist


class TesRedBlackBST(unittest.TestCase):

    def test_bst(self):
        bst = RedBlackBST()
        bst.set("e", 1)
        bst.set("a", 2)
        bst.set("m", 3)
        bst.set("i", 4)
        bst.set("d", 5)

        self.assertEqual(bst.size(), 5)
        self.assertEqual(bst.get("e"), 1)
        self.assertEqual(bst.get("m"), 3)
        self.assertEqual(bst.get("d"), 5)

        self.assertEqual(bst.min(), "a")
        self.assertEqual(bst.max(), "m")

        self.assertEqual(bst.floor("b"), "a")
        self.assertEqual(bst.ceiling("b"), "d")

        self.assertEqual(bst.select(3), "i")
        self.assertEqual(bst.rank("i"), 3)

        bst.delete_min()
        self.assertEqual(bst.size(), 4)
        self.assertEqual(bst.min(), "d")

        bst.delete_max()
        self.assertEqual(bst.size(), 3)
        self.assertEqual(bst.max(), "i")

        bst.delete("e")
        self.assertEqual(bst.size(), 2)
        self.assertEqual(bst.min(), "d")
        self.assertEqual(bst.max(), "i")

        bst = RedBlackBST()
        bst.set("e", 1)
        bst.set("a", 2)
        bst.set("m", 3)
        bst.set("i", 4)
        bst.set("d", 5)
        self.assertEqual(bst.keys_in_range("d", "i"), ["d", "e", "i"])


if __name__ == '__main__':
    unittest.main()


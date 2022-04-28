"""
Test suite for the `bst.bst` module.
"""

import unittest

import bst


class TestBinarySearchTree(unittest.TestCase):

    def test_height(self):
        test_tree = bst.BinarySearchTree()
        test_tree.insert(2)
        self.assertTrue(test_tree.height == 0)
        test_tree.insert(1)
        self.assertTrue(test_tree.height == 1)



if __name__ == "__main__":
    unittest.main()

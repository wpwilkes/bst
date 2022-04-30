"""
Test suite for the `bst.avl` module API.
"""

import unittest

import bst


class TestAVLTree(unittest.TestCase):

    def test_height(self):
        test_tree = bst.AVLTree()
        for i in range(100):
            test_tree.insert(i)
        self.assertTrue(test_tree.height < 99)

if __name__ == "__main__":
    unittest.main()

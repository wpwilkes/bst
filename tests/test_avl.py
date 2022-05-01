"""
Test suite for the `bst.avl` module API.
"""

import unittest

import bst


class TestAVLTree(unittest.TestCase):

    def test_height(self):
        test_tree = bst.AVLTree()
        for i in range(100):
            i = i * -1 if i % 2 == 0 else i
            test_tree.insert(i)
        self.assertTrue(test_tree.height < 99)
        for i in range(100):
            i = i * -1 if i % 2 == 0 else i
            test_tree.delete(i)
        self.assertTrue(test_tree.height == 0)


if __name__ == "__main__":
    unittest.main()

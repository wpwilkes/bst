"""
Test suite for the `bst.algo` module API.
"""

import unittest

import bst


class TestAlgorithms(unittest.TestCase):

    def test_traverse(self):
        test_tree = bst.BinarySearchTree()
        for i in range(5):
            test_tree.insert(i)
        keys = []
        bst.algorithms.inorder_traverse(test_tree.root,
                                        lambda n: keys.append(n.key))
        self.assertEqual(keys, [0, 1, 2, 3, 4])
        keys = []
        bst.algorithms.preorder_traverse(test_tree.root,
                                         lambda n: keys.append(n.key))
        self.assertEqual(keys, [0, 1, 2, 3, 4])
        keys = []
        bst.algorithms.postorder_traverse(test_tree.root,
                                          lambda n: keys.append(n.key))
        self.assertEqual(keys, [4, 3, 2, 1, 0])


if __name__ == "__main__":
    unittest.main()

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

    def test_is_empty(self):
        test_tree = bst.BinarySearchTree()
        self.assertTrue(test_tree.is_empty)
        test_tree.insert(0)
        self.assertFalse(test_tree.is_empty)

    def test_max(self):
        test_tree = bst.BinarySearchTree()
        test_tree.insert(2)
        test_tree.insert(1)
        test_tree.insert(3)
        self.assertTrue(test_tree.max.key == 3)

    def test_min(self):
        test_tree = bst.BinarySearchTree()
        test_tree.insert(2)
        test_tree.insert(1)
        test_tree.insert(3)
        self.assertTrue(test_tree.min.key == 1)

    def test_size(self):
        test_tree = bst.BinarySearchTree()
        self.assertTrue(test_tree.size == 0)
        test_tree.insert(0)
        self.assertTrue(test_tree.size == 1)

    def test_delete(self):
        test_tree = bst.BinarySearchTree()
        test_tree.insert(1)
        test_tree.insert(0)
        test_tree.insert(3)
        test_tree.insert(2)
        test_tree.insert(4)
        test_tree.delete(1)
        self.assertTrue(test_tree.size == 4)
        test_tree.delete(3)
        self.assertTrue(test_tree.size == 3)
        test_tree.delete(2)
        self.assertTrue(test_tree.size == 2)
        test_tree.delete(4)
        self.assertTrue(test_tree.size == 1)
        test_tree.delete(0)
        self.assertTrue(test_tree.size == 0)

    def test_find(self):
        test_tree = bst.BinarySearchTree()
        test_tree.insert(3)
        test_tree.insert(2)
        test_tree.insert(1)
        test_tree.insert(4)
        test_tree.insert(5)
        nodes = test_tree.find(1, 3)
        self.assertTrue(len(nodes) == 3)

    def test_insert(self):
        test_tree = bst.BinarySearchTree()
        test_tree.insert(1)
        self.assertTrue(test_tree.size == 1)
        test_tree.insert(0)
        self.assertTrue(test_tree.size == 2)
        test_tree.insert(2)
        self.assertTrue(test_tree.size == 3)

    def test_search(self):
        test_tree = bst.BinarySearchTree()
        self.assertTrue(test_tree.search(0) is None)
        test_tree.insert(0)
        self.assertTrue(test_tree.search(0).key == 0)

    def test_traverse(self):
        test_tree = bst.BinarySearchTree()
        for i in range(5):
            test_tree.insert(i)
        keys = []
        test_tree.traverse(bst.Traversal.INORDER,
                           lambda n: keys.append(n.key))
        self.assertEqual(keys, [0, 1, 2, 3, 4])
        keys = []
        test_tree.traverse(bst.Traversal.PREORDER,
                           lambda n: keys.append(n.key))
        self.assertEqual(keys, [0, 1, 2, 3, 4])
        keys = []
        test_tree.traverse(bst.Traversal.POSTORDER,
                           lambda n: keys.append(n.key))
        self.assertEqual(keys, [4, 3, 2, 1, 0])


if __name__ == "__main__":
    unittest.main()

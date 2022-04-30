"""
Implementation of AVL tree.
"""

from typing import Any, Optional

from bst.bst import BinarySearchTree
from bst.node import Node
from bst.updates import delete, insert
import bst.algo as algorithms

class AVLTree(BinarySearchTree):

    def _leftRotate(self, z):
        y = z.right
        z.right = y.left
        if y.left:
            y.left.parent = z
        y.parent = z.parent
        if z.parent == None:
            self._root = y
            pass
        elif z == z.parent.left:
            z.parent.left = y
        else:
            z.parent.right = y
        y.left = z
        z.parent = y

    def _rightRotate(self, z):
        y = z.left
        z.left = y.right
        if y.right:
            y.right.parent = z

        y.parent = z.parent
        if z.parent == None:
            self._root = y
        elif z == z.parent.right:
            z.parent.right = y
        else:
            z.parent.left = y
        y.right = z
        z.parent = y

    def insert(self, key: int, value: Optional[Any] = None) -> None:
        """
        """
        if self._root is None:
            self._root = Node(key, value)
        else:
            insert(self._root, key, value, self._insert_fix)

    def _insert_fix(self, node, key):
        """
        """
        balance = algorithms.balance(node)
        if balance > 1:
            if key < node.left.key:
                self._rightRotate(node)
            elif key > node.left.key:
                self._leftRotate(node.left)
                self._rightRotate(node)
        if balance < -1:
            if key > node.right.key:
                self._leftRotate(node)
            elif key < node.right.key:
                self._rightRotate(node.right)
                self._leftRotate(node)

    def delete(self, key: int) -> None:
        """
        """
        delete(self._root, key, self._delete_fix)

    def _delete_fix(self, node:Optional[Node], key: int) -> Optional[Node]:
        """
        """
        if node:
            balance = algorithms.balance(node)
            if balance > 1:
                if algorithms.balance(node.left) >= 0:
                    self._rightRotate(node)
                elif algorithms.balance(node.left) < 0:
                    self._leftRotate(node.left)
                    self._rightRotate(node)
            if balance < -1:
                if algorithms.balance(node.right) <= 0:
                    self._leftRotate(node)
                elif algorithms.balance(node.right) > 0:
                    self._rightRotate(node.right)
                    self._leftRotate(node)

"""
Implementation of an AVL tree.
"""

from typing import Any, Optional

from bst.bst import BinarySearchTree
import bst.fixes as fixes
import bst.updates as updates


class AVLTree(BinarySearchTree):
    """
    Implementation of an AVL tree.
    """

    def insert(self, key: int, value: Optional[Any] = None) -> None:
        """
        Insert a node in the tree with the given key and value.

        Parameters
        ----------
        key : int
            The key to insert.
        value : any, optional
            The value to insert. Default is None.
        """
        self._root = updates.insert(self._root, key, value, fixes.avl_insert_fix)

    def delete(self, key: int) -> None:
        """
        Remove a node from the tree with the given key.

        Parameters
        ----------
        key : int
            The key of the node to remove.
        """
        self._root = updates.delete(self._root, key, fixes.avl_delete_fix)

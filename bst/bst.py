"""
Implementation of a binary search tree.
"""

from typing import Any, Optional

from bst.node import Node
import bst.algo as algorithms
import bst.updates as updates


class BinarySearchTree:
    """
    Implementation of a binary search tree.
    """

    def __init__(self):
        """
        Instantiate a binary search tree.
        """
        self._root : Optional[Node] = None

    @property
    def height(self) -> Optional[int]:
        """
        Compute the height of the tree.
        """
        return algorithms.height(self._root)

    @property
    def is_empty(self) -> bool:
        """
        Determine if the tree is empty.
        """
        return self._root is None

    @property
    def max(self) -> Optional[Node]:
        """
        Find the node in the tree with max key (if any).
        """
        if self._root:
            return algorithms.max(self._root)

    @property
    def min(self) -> Optional[Node]:
        """
        Find the node in the tree with min key (if any).
        """
        if self._root:
            return algorithms.min(self._root)

    @property
    def root(self) -> Optional[Node]:
        """
        Access the tree's root node (if any).
        """
        return self._root

    def delete(self, key: int) -> None:
        """
        Remove a node from the tree with the given key.

        Parameters
        ----------
        key : int
            The key to remove.
        """
        self._root = updates.delete(self._root, key, None)

    def insert(self,
               key: int,
               value: Optional[Any] = None) -> None:
        """
        Insert a node in the tree with the given key and value.

        Parameters
        ----------
        key : int
            The key to insert.
        value : any, optional
            The value to insert. Default is None.
        """
        self._root = updates.insert(self._root, key, value, None)

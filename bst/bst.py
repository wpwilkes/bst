"""
Implementation of a binary search tree.
"""

from typing import Any, Optional

from bst.node import Node
from bst.updates import delete, insert
import bst.algo as algorithms


class BinarySearchTree:
    """
    """

    def __init__(self):
        self._root : Optional[Node] = None

    @property
    def height(self) -> Optional[int]:
        """
        """
        return algorithms.height(self._root)

    @property
    def is_empty(self) -> bool:
        """
        """
        return self._root is None

    @property
    def max(self) -> Optional[Node]:
        """
        """
        return algorithms.max(self._root)

    @property
    def min(self) -> Optional[Node]:
        """
        """
        return algorithms.min(self._root)

    @property
    def root(self) -> Optional[Node]:
        """
        """
        return self._root

    def delete(self, key: int) -> None:
        """
        """
        self._root = delete(self._root, key)

    def insert(self, key: int, value: Optional[Any] = None) -> None:
        """
        """
        if self._root is None:
            self._root = Node(key, value)
        else:
            insert(self._root, key, value)

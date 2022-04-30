"""
Implementation of a binary search tree.
"""

from typing import Any, Optional

from bst.node import Node
import bst.algo as algorithms


class BinarySearchTree:
    """
    """

    def __init__(self):
        self._root : Optional[Node] = None
        self._size : int = 0

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

    @property
    def size(self) -> int:
        """
        """
        return self._size

    def delete(self, key: int) -> None:
        """
        """
        if self._root:
            self._root = self._delete(self._root, key)

    def _delete(self, node:Optional[Node], key: int) -> Optional[Node]:
        """
        """
        if node is None:
            return None
        elif key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        elif node.left and node.right:
            temp = algorithms.min(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete(node.right, temp.key)
        else:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            self._size -= 1
        return node

    def insert(self, key: int, value: Optional[Any] = None) -> None:
        """
        """
        if self._root is None:
            self._root = Node(key, value)
        else:
            self._insert(self._root, key, value)
        self._size += 1

    def _insert(self, node: Node, key: int, value: Any) -> None:
        """
        """
        if key <= node.key:
            if node.left:
                self._insert(node.left, key, value)
            else:
                node.left = Node(key, value)
        else:
            if node.right:
                self._insert(node.right, key, value)
            else:
                node.right = Node(key, value)

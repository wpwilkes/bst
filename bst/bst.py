"""
Implementation of a binary search tree.
"""

from typing import Any, Callable, Optional

from .node import Node
from .traversal import Traversal


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
        if self._root:
            return self._height(self._root)

    @property
    def is_empty(self) -> bool:
        """
        """
        return self._root is None

    @property
    def max(self) -> Optional[Node]:
        """
        """
        if self._root:
            return self._max(self._root)

    @property
    def min(self) -> Optional[Node]:
        """
        """
        if self._root:
            return self._min(self._root)

    @property
    def size(self) -> int:
        """
        """
        return self._size

    def _height(self, node: Node) -> int:
        if node.left is None and node.right is None:
            return 0
        else:
            h = max(self._height(node.left) if node.left else 0,
                    self._height(node.right) if node.right else 0)
            return 1 + h

    def _max(self, node: Node) -> Node:
        """
        """
        while node.right is not None:
            node = node.right
        return node

    def _min(self, node: Node) -> Node:
        """
        """
        while node.left is not None:
            node = node.left
        return node

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
            temp = self._min(node.right)
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

    def search(self, key: int) -> Optional[Node]:
        """
        """
        if self._root:
            return self._search(self._root, key)

    def _search(self, node: Node, key: int) -> Optional[Node]:
        if key == node.key:
            return node
        if key <= node.key:
            if node.left:
                return self._search(node.left, key)
        else:
            if node.right:
                return self._search(node.right, key)

    def traverse(self,
                 order: Traversal,
                 visit: Callable[[Node], Any]) -> None:
        """
        """
        if self._root:
            self._traverse(self._root, order, visit)

    def _traverse(self,
                  node: Node,
                  order: Traversal,
                  visit: Callable[[Node], Any]) -> None:
        """
        """
        if order == Traversal.PREORDER:
            visit(node)
            if node.left:
                self._traverse(node.left, order, visit)
            if node.right:
                self._traverse(node.right, order, visit)
        elif order == Traversal.INORDER:
            if node.left:
                self._traverse(node.left, order, visit)
            visit(node)
            if node.right:
                self._traverse(node.right, order, visit)
        elif order == Traversal.POSTORDER:
            if node.left:
                self._traverse(node.left, order, visit)
            if node.right:
                self._traverse(node.right, order, visit)
            visit(node)

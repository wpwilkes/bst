"""
Implementation of binary search tree algorithms.
"""

from typing import Any, Callable, Optional
import builtins

from bst.node import Node


def balance(node: Node) -> int:
    """
    """
    return height(node.left) - height(node.right)


def height(node: Optional[Node]) -> int:
    """
    """
    if node is None:
        return 0
    elif (node.left is None) and (node.right is None):
        return 0
    else:
        return 1 + builtins.max(height(node.left), height(node.right))


def inorder_traverse(node: Optional[Node],
                     visit: Callable[[Node], Any]) -> None:
    """
    """
    if node is None:
        return None
    inorder_traverse(node.left, visit)
    visit(node)
    inorder_traverse(node.right, visit)


def max(node: Optional[Node]) -> Optional[Node]:
    """
    """
    if node is None:
        return None
    while node.right is not None:
        node = node.right
    return node


def min(node: Optional[Node]) -> Optional[Node]:
    """
    """
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node


def preorder_traverse(node: Optional[Node],
                      visit: Callable[[Node], Any]) -> None:
    """
    """
    if node is None:
        return None
    visit(node)
    preorder_traverse(node.left, visit)
    preorder_traverse(node.right, visit)


def postorder_traverse(node: Optional[Node],
                       visit: Callable[[Node], Any]) -> None:
    """
    """
    if node is None:
        return None
    postorder_traverse(node.left, visit)
    postorder_traverse(node.right, visit)
    visit(node)


def search(node: Optional[Node], key: int) -> Optional[Node]:
    """
    """
    if node is None:
        return None
    elif key == node.key:
        return node
    elif key <= node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)


def search_range(node: Optional[Node], min_key: int, max_key: int):
    if node is None:
        return []
    if (min_key <= node.key) and (node.key <= max_key):
        L = search_range(node.left, min_key, max_key)
        R = search_range(node.right, min_key, max_key)
        return L + [node] + R
    elif min_key > node.key:
        return search_range(node.right, min_key, max_key)
    elif max_key < node.key:
        return search_range(node.left, min_key, max_key)

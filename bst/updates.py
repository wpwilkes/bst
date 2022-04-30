"""
"""

from typing import Any, Callable, Optional

from bst.node import Node
import bst.algo as algorithms


def delete(node:Optional[Node],
           key: int,
           restructure: Optional[Callable] = None) -> Optional[Node]:
    """
    """
    if node is None:
        return None
    elif key < node.key:
        node.left = delete(node.left, key, restructure)
    elif key > node.key:
        node.right = delete(node.right, key, restructure)
    elif node.left and node.right:
        temp = algorithms.min(node.right)
        node.key = temp.key
        node.value = temp.value
        node.right = delete(node.right, temp.key, restructure)
    else:
        if node.left is None:
            node = node.right
        elif node.right is None:
            node = node.left
    if restructure:
        restructure(node)
    return node


def insert(node: Node,
           key: int,
           value: Any,
           restructure: Optional[Callable] = None) -> None:
    """
    """
    if key <= node.key:
        if node.left:
            insert(node.left, key, value, restructure)
        else:
            node.left = Node(key, value)
    else:
        if node.right:
            insert(node.right, key, value, restructure)
        else:
            node.right = Node(key, value)
    if restructure:
        restructure(node)

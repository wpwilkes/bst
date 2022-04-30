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
            if node.right:
                node.right.parent = node.parent
            node = node.right
        elif node.right is None:
            if node.left:
                node.left.parent = node.parent
            node = node.left
    if restructure:
        restructure(node, key)
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
            new_node = Node(key, value)
            new_node.parent = node
            node.left = new_node
    else:
        if node.right:
            insert(node.right, key, value, restructure)
        else:
            new_node = Node(key, value)
            new_node.parent = node
            node.right = new_node
    if restructure:
        restructure(node, key)

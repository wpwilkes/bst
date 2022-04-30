"""
"""

from typing import Optional

from bst.node import Node
import bst.algo as algorithms
import bst.rotations as rotations


def avl_delete_fix(node:Optional[Node], key: int) -> Optional[Node]:
    """
    """
    if node:
        balance = algorithms.balance(node)
        if balance > 1:
            if algorithms.balance(node.left) >= 0:
                rotations.right_rotate(node)
            elif algorithms.balance(node.left) < 0:
                rotations.left_right_rotate(node)
        if balance < -1:
            if algorithms.balance(node.right) <= 0:
                rotations.left_rotate(node)
            elif algorithms.balance(node.right) > 0:
                rotations.right_left_rotate(node)
    return node


def avl_insert_fix(node: Node, key: int) -> Node:
    """
    """
    balance = algorithms.balance(node)
    if balance > 1:
        if key < node.left.key:
            node = rotations.right_rotate(node)
        elif key > node.left.key:
            node = rotations.left_right_rotate(node)
    if balance < -1:
        if key > node.right.key:
            node = rotations.left_rotate(node)
        elif key < node.right.key:
            node = rotations.right_left_rotate(node)
    return node

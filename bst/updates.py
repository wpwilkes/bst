"""
Implementation of binary search tree update operations.
"""

from typing import Any, Callable, Optional

from bst.node import Node
import bst.algo as algorithms


def delete(node:Optional[Node],
           key: int,
           restructure: Optional[Callable] = None) -> Optional[Node]:
    """
    Remove a node with key from the tree rooted at node.

    Parameters
    ----------
    node : Node
        The root of a tree.
    key : int
        The key to remove from the tree.
    restructure : callable, optional
        A method to restructure the tree rooted at node.
        Default is None.

    Returns
    -------
    node :
        The tree with the key removed.
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
           value: Optional[Any] = None,
           restructure: Optional[Callable] = None) -> None:
    """
    Insert the key-value pair into the tree rooted at node.

    Parameters
    ----------
    node : Node
        The root of a tree.
    key : int
        The new node's key.
    value : any, optional
        The new node's value. Default is None.
    restructure : callable, optional
        A method to restructure the tree rooted at node.
        Default is None.
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

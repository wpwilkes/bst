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
            if node.right:
                node.right.parent = node.parent
            node = node.right
        elif node.right is None:
            if node.left:
                node.left.parent = node.parent
            node = node.left
    if restructure:
        node = restructure(node, key)
    return node


def insert(node: Optional[Node],
           key: int,
           value: Optional[Any] = None,
           restructure: Optional[Callable[[Node, int], Node]] = None) -> Node:
    """
    Insert the key-value pair into the tree rooted at node.

    Parameters
    ----------
    node : Node, optional
        The root of a tree.
    key : int
        The new node's key.
    value : any, optional
        The new node's value. Default is None.
    restructure : callable, optional
        A method to restructure the tree rooted at node.
        Default is None.

    Returns
    -------
    node : Node
        The updated tree rooted at node.
    """
    if node is None:
        node = Node(key, value)
    elif key <= node.key:
        node.left = insert(node.left, key, value, restructure)
        node.left.parent = node
    else:
        node.right = insert(node.right, key, value, restructure)
        node.right.parent = node
    if restructure:
        node = restructure(node, key)
    return node

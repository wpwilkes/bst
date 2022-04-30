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


def depth(node: Optional[Node]) -> int:
    """
    Compute the depth of a node.

    Parameters
    ----------
    node : node, optional
        The node whose depth will be computed.

    Returns
    -------
    int :
        The node's depth.
    """
    if node is None:
        return 0
    else:
        return 1 + depth(node.parent)


def height(node: Optional[Node]) -> int:
    """
    Compute the height of a node.

    Parameters
    ----------
    node : node, optional
        The node whose height will be computed.

    Returns
    -------
    int :
        The node's height.
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
    Traverse any tree rooted at the given node in an inorder manner.

    Parameters
    ----------
    node : optional, node
        The node to begin the traversal at.
    visit : callable
        The visit action to perform at the nodes.
    """
    if node is None:
        return None
    inorder_traverse(node.left, visit)
    visit(node)
    inorder_traverse(node.right, visit)


def max(node: Node) -> Node:
    """
    Find the node with max key for the tree rooted at the given node.

    Parameters
    ----------
    node : Node
        The root of a tree.

    Returns
    -------
    node : Node
        The node with max key.
    """
    while node.right is not None:
        node = node.right
    return node


def min(node: Node) -> Node:
    """
    Find the node with min key for the tree rooted at the given node.

    Parameters
    ----------
    node : Node
        The root of a tree.

    Returns
    -------
    node : Node
        The node with min key.
    """
    while node.left is not None:
        node = node.left
    return node


def postorder_traverse(node: Optional[Node],
                       visit: Callable[[Node], Any]) -> None:
    """
    Traverse any tree rooted at the given node in a postorder manner.

    Parameters
    ----------
    node : optional, node
        The node to begin the traversal at.
    visit : callable
        The visit action to perform at the nodes.
    """
    if node is None:
        return None
    postorder_traverse(node.left, visit)
    postorder_traverse(node.right, visit)
    visit(node)


def preorder_traverse(node: Optional[Node],
                      visit: Callable[[Node], Any]) -> None:
    """
    Traverse any tree rooted at the given node in a preorder manner.

    Parameters
    ----------
    node : optional, node
        The node to begin the traversal at.
    visit : callable
        The visit action to perform at the nodes.
    """
    if node is None:
        return None
    visit(node)
    preorder_traverse(node.left, visit)
    preorder_traverse(node.right, visit)


def search(node: Optional[Node], key: int) -> Optional[Node]:
    """
    Perform binary search starting at the tree rooted at given node.

    Parameters
    ----------
    node : Node, optional
        The node to begin searching at.
    key : int
        The key to search for.

    Returns
    -------
    Node, optional :
        The node if it is found; otherwise, None.
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
    """
    Perform a range query at the tree rooted at the given node.

    Parameters
    ----------
    node : Node, optional
        The node to begin searching at.
    min_key : int
        The minimum key to include in the range.
    max_key : int
        The maximum key to include in the range.

    Returns
    -------
    list :
        A list of nodes with keys in the range of (min_key, max_key)
        if any exist. Otherwise, an empty list is returned.
    """
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

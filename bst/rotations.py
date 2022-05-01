"""
Implementation of binary search tree node rotations.
"""

from bst.node import Node


def left_rotate(z: Node) -> Node:
    """
    Perform a left rotation about the given node.
    """
    if not z.right:
        raise ValueError("Left rotate about a node with no right child.")
    y = z.right
    z.right = y.left
    if y.left:
        y.left.parent = z
    y.parent = z.parent
    if z.parent:
        if z == z.parent.left:
            z.parent.left = y
        else:
            z.parent.right = y
    y.left = z
    z.parent = y
    return y


def left_right_rotate(z: Node) -> Node:
    """
    Perform a left-right rotation about the given node.
    """
    if not z.left:
        raise ValueError("Left-right rotate about a node with no left child.")
    return right_rotate(left_rotate(z.left))


def right_rotate(z: Node) -> Node:
    """
    Perform a right rotation about the given node.
    """
    if not z.left:
        raise ValueError("Right rotate about a node with no left child.")
    y = z.left
    z.left = y.right
    if y.right:
        y.right.parent = z
    y.parent = z.parent
    if z.parent:
        if z == z.parent.right:
            z.parent.right = y
        else:
            z.parent.left = y
    y.right = z
    z.parent = y
    return y


def right_left_rotate(z: Node) -> Node:
    """
    Perform a right-left rotation about the given node.
    """
    if not z.right:
        raise ValueError("Right-left rotate about a node with no right child.")
    return left_rotate(right_rotate(z.right))

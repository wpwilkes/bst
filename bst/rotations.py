"""
Implementation of binary search tree node rotations.
"""

from bst.node import Node


def left_rotate(z: Node) -> Node:
    """
    """
    if not z.right:
        raise ValueError
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
    """
    if not z.left:
        raise ValueError
    return right_rotate(left_rotate(z.left))


def right_rotate(z: Node) -> Node:
    """
    """
    if not z.left:
        raise ValueError
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
    """
    if not z.right:
        raise ValueError
    return left_rotate(right_rotate(z.right))

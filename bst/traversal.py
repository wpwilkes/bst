"""
Enumerate binary search tree traversals.
"""

from enum import Enum


class Traversal(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

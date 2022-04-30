"""
Implementation of a binary search tree node.
"""

from typing import Any, Optional


class Node:
    """
    """

    def __init__(self, key: int, value: Optional[Any] = None):
        self.key = key
        self.value = value
        self.left : Optional[Node] = None
        self.right : Optional[Node] = None
        self.parent: Optional[Node] = None

    def __repr__(self):
        """
        """
        return f"Node(key={str(self.key)}, value={str(self.value)})"

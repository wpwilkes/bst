"""
Implementation of a binary search tree node.
"""

from typing import Any, Optional


class Node:
    """
    Implementation of a binary search tree node.
    """

    def __init__(self,
                 key: int,
                 value: Optional[Any] = None):
        """
        Instantiate a binary search tree node.

        Parameters
        ----------
        key : int
            The node's key for comparisons.
        value : any, optional
            The data to store in the node. Defualt is None.
        """
        self.key = key
        self.value = value
        self.left : Optional[Node] = None
        self.right : Optional[Node] = None
        self.parent : Optional[Node] = None

    def __repr__(self) -> str:
        """
        Produce a string representation of the node.

        Returns
        -------
        str :
            The string representation.
        """
        return f"Node(key={str(self.key)}, value={str(self.value)})"

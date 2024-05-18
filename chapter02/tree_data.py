from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Tree:
    value: int
    left_child: Tree | None = None
    right_child: Tree | None = None


tree_01 = Tree(
    value=1,
    left_child=Tree(
        value=2,
        left_child=Tree(
            value=4,
        ),
        right_child=Tree(
            value=5,
        ),
    ),
    right_child=Tree(
        value=3,
        left_child=Tree(
            value=6,
            right_child=Tree(value=7),
        ),
    ),
)
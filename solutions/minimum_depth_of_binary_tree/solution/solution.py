from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        nodes = [(root, 1)]

        for node, lvl in nodes:
            if node.left is None and node.right is None:
                return lvl

            if node.left:
                nodes.append((node.left, lvl + 1))
            if node.right:
                nodes.append((node.right, lvl + 1))

        return nodes[-1][1]

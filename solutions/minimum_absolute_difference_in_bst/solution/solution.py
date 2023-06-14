from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_minimum_difference(self, root: Optional[TreeNode]) -> int:
        self.result = 100001
        self.prev_value = None

        def sorting_node_values(node):
            if node.left is not None:
                sorting_node_values(node.left)

            if self.prev_value is not None:
                self.result = min(self.result, node.val - self.prev_value)
            self.prev_value = node.val

            if node.right is not None:
                sorting_node_values(node.right)

        sorting_node_values(root)

        return self.result

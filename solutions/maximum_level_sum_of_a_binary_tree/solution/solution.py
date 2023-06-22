class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_level_sum(self, root: TreeNode) -> int:
        m = float('-inf')
        result = 1
        level = 0
        items = [root]

        while items:
            level += 1
            sum_ = sum(i.val for i in items)

            if sum_ > m:
                m = sum_
                result = level

            new_items = []

            for node in items:
                if node.left is not None:
                    new_items.append(node.left)
                if node.right is not None:
                    new_items.append(node.right)
            items = new_items
        return result

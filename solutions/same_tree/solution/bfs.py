import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        queue = collections.deque()

        queue.append((p, q))

        while queue:
            p_child, q_child = queue.popleft()

            if p_child is None and q_child is None:
                continue

            if p_child is None or q_child is None:
                return False

            if p_child.val != q_child.val:
                return False

            queue.append((p_child.left, q_child.left))
            queue.append((p_child.right, q_child.right))

        return True

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_equal(lhs: TreeNode | None, rhs: TreeNode | None):
    if lhs is None:
        return rhs is None
    if rhs is None:
        return False

    if lhs.val != rhs.val:
        return False
    return is_equal(lhs.left, rhs.right) and is_equal(lhs.right, rhs.left)


class Solution:
    def is_symmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        return is_equal(root.left, root.right)

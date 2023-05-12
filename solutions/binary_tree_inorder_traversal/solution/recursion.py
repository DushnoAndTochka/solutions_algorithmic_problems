
def inorder_traversal(node):
    if node is None:
        return
    yield from inorder_traversal(node.left)
    yield node
    yield from inorder_traversal(node.right)


class Solution:
    def inorder_traversal(self, root) -> list[int]:
        return [node.val for node in inorder_traversal(root)]

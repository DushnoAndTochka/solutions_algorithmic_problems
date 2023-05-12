class Solution:
    def flatten(self, root) -> None:
        if root is None:
            return

        stack = []
        prev = root

        self._add_from_node(stack, root)

        while stack:
            node = stack.pop()
            prev.right = node
            prev.left = None
            self._add_from_node(stack, node)
            prev = node

        prev.left = None

    def _add_from_node(self, stack, node):
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

def walk(node):
    if node is None:
        return
    left = node.left
    right = node.right

    yield node
    yield from walk(left)
    yield from walk(right)


class Solution:
    def flatten(self, root) -> None:
        if root is None:
            return None

        it = walk(root)
        current = next(it)

        for next_ in it:
            current.right = next_
            current.left = None
            current = next_

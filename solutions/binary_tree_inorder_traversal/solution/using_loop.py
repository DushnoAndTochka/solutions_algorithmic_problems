class Solution:
    def inorder_traversal(self, root) -> list[int]:
        result = []
        stack = []
        current = root

        while True:

            if current is not None:
                stack.append(current)
                current = current.left

            elif stack:

                current = stack.pop()
                result.append(current.val)
                current = current.right
            else:
                break
        return result

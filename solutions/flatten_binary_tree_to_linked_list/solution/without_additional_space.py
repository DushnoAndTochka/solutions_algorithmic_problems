class Solution:
    def flatten(self, root):
        current = root
        while current is not None:

            if current.left is not None:
                previous = current.left

                while previous.right is not None:
                    previous = previous.right

                previous.right = current.right
                current.right = current.left
                current.left = None
            current = current.right

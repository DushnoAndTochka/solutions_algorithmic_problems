class Solution:
    def level_order(self, root) -> list[list[int]]:
        result = []
        if root is None:
            return result

        level = [root]

        while level:
            result.append([i.val for i in level])
            next_level = []
            for i in level:
                next_level.extend(i.children)
            level = next_level
        return result

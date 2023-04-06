class Solution:
    def max_distance(self, colors: list[int]) -> int:
        result = 0
        length = len(colors)
        first = colors[0]
        last = colors[-1]
        for i, color in enumerate(colors):
            if color != first:
                result = max(result, i)
            if color != last:
                result = max(result, length - 1 - i)
        return result

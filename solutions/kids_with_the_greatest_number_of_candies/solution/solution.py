class Solution:

    def kids_with_candies(self, candies: list[int], extra: int) -> list[bool]:
        m = max(candies) - extra
        return [i >= m for i in candies]

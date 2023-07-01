import math


class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)

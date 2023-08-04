class Solution:
    def single_non_duplicate(self, nums: list[int]) -> int:
        result = 0

        for i in nums:
            result ^= i

        return result

class Solution:
    def array_sign(self, nums: list[int]) -> int:
        result = 1

        for num in nums:
            if num == 0:
                return 0

            if num < 0:
                result = -result

        return result

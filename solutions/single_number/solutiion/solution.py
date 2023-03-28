class Solution:
    def single_number(self, nums: list[int]) -> int:
        xor_counter = 0
        for i in nums:
            xor_counter ^= i
        return xor_counter

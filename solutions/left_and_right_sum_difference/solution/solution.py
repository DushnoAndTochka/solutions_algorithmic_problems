class Solution:
    def left_rigth_difference(self, nums: list[int]) -> list[int]:
        right = sum(nums)
        left = 0
        r = []
        for num in nums:
            right -= num
            r.append(abs(right - left))
            left += num
        return r

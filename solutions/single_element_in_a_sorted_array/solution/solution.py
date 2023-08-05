class Solution:
    def single_non_duplicate(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1 or nums[0] != nums[1]:
            return nums[0]
        if nums[-2] != nums[-1]:
            return nums[-1]

        lp = 1
        rp = n - 2

        while lp <= rp:
            mp = (lp + rp) // 2

            if nums[mp] != nums[mp - 1] and nums[mp] != nums[mp + 1]:
                return nums[mp]
            if (
                mp % 2 == 1
                and nums[mp] == nums[mp - 1]
                or mp % 2 == 0
                and nums[mp] == nums[mp + 1]
            ):
                lp = mp + 1
            else:
                rp = mp - 1

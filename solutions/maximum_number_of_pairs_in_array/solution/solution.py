class Solution:
    def number_of_pairs(self, nums: list[int]) -> list[int]:
        encountered_nums = dict()
        res = [0, 0]

        for num in nums:
            if encountered_nums.get(num):
                encountered_nums[num] -= 1
                res[0] += 1
                res[1] -= 1
            else:
                encountered_nums[num] = 1
                res[1] += 1

        return res

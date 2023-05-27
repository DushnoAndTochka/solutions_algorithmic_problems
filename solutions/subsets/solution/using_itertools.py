import itertools


class Solution:
    def subsets(self, nums: list[int]) -> list[tuple[int]]:
        r = [(), tuple(nums)]
        for i in range(1, len(nums)):
            r.extend(itertools.combinations(nums, i))
        return r

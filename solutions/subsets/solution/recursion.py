
class Solution:

    def subsets(self, nums: list[int]) -> list[list[int]]:
        it = self._subsets(nums, [], 0)
        return list(it)

    def _subsets(self, nums: list[int], item: list[int], i: int):
        if i >= len(nums):
            yield item.copy()
            return
        item.append(nums[i])
        yield from self._subsets(nums, item, i + 1)
        item.pop()
        yield from self._subsets(nums, item, i + 1)

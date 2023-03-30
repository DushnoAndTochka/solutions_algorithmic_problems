class Solution:
    def majority_element(self, nums: list[int]) -> int:
        it = iter(nums)
        count = 1
        item = next(it)
        for num in it:
            if count == 0:
                item = num

            if item == num:
                count += 1
            else:
                count -= 1

        return item

import itertools


def to_str(start, end):
    return f'{start}->{end}' if start != end else str(start)


class Solution:
    def summary_ranges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        end = start = nums[0]
        result = []

        for num in itertools.islice(nums, 1, len(nums)):
            if num != end + 1:
                result.append(to_str(start, end))
                start = num
            end = num
        result.append(to_str(start, end))
        return result

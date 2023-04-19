import heapq
from collections import Counter


class Solution:
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums

        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

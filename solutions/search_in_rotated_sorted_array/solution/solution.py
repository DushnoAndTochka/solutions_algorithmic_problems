from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] <= nums[-1]:
            # Если первое число меньше последнего, значит не было разрыва.
            # Можем сразу использовать бинарный поиск.
            return self.binary_search(nums, target)

        gap_number = self.search_gap(nums)

        if nums[0] <= target <= nums[gap_number - 1]:
            # Если наш таргет в массиве до разрыва, то ищем там
            return self.binary_search(nums, target, rigth=gap_number - 1)

        if nums[gap_number] <= target <= nums[-1]:
            # Если наш таргет в массиве после разрыва, то ищем там
            return self.binary_search(nums, target, left=gap_number)

        # если оба условия не удовлетворили,
        # значи наше чило вообще не в nums
        return -1

    def binary_search(
            self, nums: List[int], target: int, left=0, rigth=None) -> int:
        if rigth is None:
            rigth = len(nums) - 1

        while left <= rigth:
            mid = (left + rigth) // 2

            if target == nums[mid]:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                rigth = mid - 1
        return -1

    def search_gap(self, nums: List[int]) -> int:
        left, rigth = 0, len(nums) - 1

        while left <= rigth:
            mid = (left + rigth) // 2

            if nums[mid] < nums[mid - 1] and mid - 1 >= 0:
                return mid

            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                rigth = mid - 1

        return -1

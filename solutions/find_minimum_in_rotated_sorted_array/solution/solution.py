from typing import List


class Solution:
    def solution(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            # Если последний элемент больше первого,
            # значит ротации не было. 
            # А это значит что первый элемент является минимальным.
            return nums[0]
        else:
            gap_index = self.search_gap(nums)
            return nums[gap_index]


    def search_gap(self, nums: List[int]) -> int:
        left, rigth = 0, len(nums) -1

        while left <= rigth:
            mid = (left + rigth) // 2

            if nums[mid] < nums[mid-1] and mid-1 >= 0:
                # Если текующий элемент оказался меньше предыдущего,
                # значит мы нашли место разрыва. Этот индекс и будет ответом.
                return mid
            elif nums[mid] >= nums[0]:
                # Если текущая середина больше или равна первому,
                # значит разрыв находится правее.
                left = mid + 1
            else:
                # Если текущее чило меньше первого,
                # значит оно находится после разрыва. И надо искать левее.
                rigth = mid - 1

        return -1

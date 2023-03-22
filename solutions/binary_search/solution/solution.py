from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # границы в которых мы ищем нужное нам число
        left, rigth = 0, len(nums) -1

        while left <= rigth:
            # середина текущей границы.
            mid = (left + rigth) // 2

            if target == nums[mid]:
                # если середина равна, значит и ответ найден
                return mid
            elif nums[mid] < target:
                # Если target оказался "правее"(больше) середины, 
                # значит надо искать там. 
                # Сдвигаем левую границу правее середины и ищем в новой области.
                left = mid + 1
            else:
                # Если target оказался "левее"(меньше) середины, 
                # значит надо искать там. 
                # Сдвигаем правую границу левее середины и ищем в новой области.
                rigth = mid - 1

        return -1
        
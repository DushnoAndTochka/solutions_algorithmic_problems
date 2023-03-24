from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        left, right = 0, len(nums) - 1

        while left <= right:
            # ищем середину
            mid = (left + right) // 2
            
            if nums[mid] == target:
                # равны, значит нашли
                return True
            
            if nums[mid] == nums[left]:
                # Если середина равна левому,
                # то стоит понять есть ли там еще уникальные числа.
                # В худшем случае это приведет к линейному поиску.
                left += 1
                continue
            elif nums[mid] == nums[right]:
                right -= 1
                continue
                
            if nums[mid] > nums[right]:
                # Значит справа от середины есть разрыв
                if nums[left] <= target < nums[mid]:
                    # значит наше число в левой,
                    # отсортированной части.
                    right = mid - 1
                else:
                    # в левой не нашли ? давай искать в месте с разрывом.
                    left = mid + 1
            elif nums[mid] < nums[right]:
                # Значит справа нет разрыва
                if nums[mid] < target <= nums[right]:
                    # значит число лежит в отсортированном куске справа.
                    left = mid + 1
                else:
                    # ищем слева
                    right = mid - 1
            else:
                # Если середина равна правому,
                # то стоит понять есть ли там еще уникальные числа.
                # В худшем случае это приведет к линейному поиску.
                right -= 1
                

        return False

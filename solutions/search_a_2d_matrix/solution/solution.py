from typing import List, Union


def query_row_search(matrix: List[List[int]], target: int, mid: int) -> int:
    """
    вспомогательная ф-ция, 
    которая позволяет понять куда двигаться при бин поиске нужной строки.

    1 - двигаемя вправо
    -1 - двигаемся влево
    0 - мы нашли
    """
    if matrix[mid][0] <= target <= matrix[mid][-1]:
        return 0
    elif matrix[mid][0] > target:
        return -1
    else:
        return 1
    

def query_target_search(nums: List[int], target: int, mid: int) -> int:
    """
    вспомогательная ф-ция, 
    которая позволяет понять куда двигаться при бин поиске в строке.

    1 - двигаемя вправо
    -1 - двигаемся влево
    0 - мы нашли
    """
    if target == nums[mid]:
        return 0
    elif nums[mid] > target:
        return -1
    else:
        return 1


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Ищем нужную нам строку.
        row_index = self.binary_search(matrix, target, query_row_search)
        target_index = -1
        if row_index != -1:
            # Усли строка была найдена, то ищем в ней target
            row = matrix[row_index]
            target_index = self.binary_search(
                row,
                target, 
                query_target_search
            )

        # Отвечаем был ли найден таргет
        return target_index != -1
    

    def binary_search(
            self,
            nums: Union[List[int], List[List[int]]],
            target: int,
            query: callable
    ) -> bool:
        """
        Классический бинарный поиск. 
        О нем можно почитать в задаче binary_search.
        """
        left, rigth = 0, len(nums) -1

        while left <= rigth:
            mid = (left + rigth) // 2
            print(left, mid, rigth)
            # используем callable, который прокидывается в ф-цию
            # Можно использовать класс с ф-циями, 
            # что бы контракт поведения точно не был нарушен.
            query_response = query(nums, target, mid)
            if query_response == 0:
                return mid
            elif query_response == 1:
                left = mid + 1
            elif query_response == -1:
                rigth = mid - 1

        return -1

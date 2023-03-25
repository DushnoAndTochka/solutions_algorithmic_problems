from typing import List


class Solution(object):

    def two_sum(self, nums: List[int], target: int) -> List[int]:

        # создаем hasm_m для хранения уже встреченных чисел и индексов
        checked = {}
        for i, num in enumerate(nums):
            # берем разность между таргетом и текущем числом,
            # тем самым получаем число, которого нам не хватает
            any_num = target - num
            if any_num in checked:
                # Если мы его нашли в hash_m, значит мы его встречали раньше.
                #  Значит пора давать ответ
                return list((i, checked[any_num]))

            # Если не нашли в hash_m, значит его надо запомнить.
            # Вдруг впереди есть его "пара", которая в сумме и даст таргет.
            checked[num] = i

        return [-1, -1]

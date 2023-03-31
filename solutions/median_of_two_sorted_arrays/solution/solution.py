class Solution:
    def __init__(self) -> None:
        super().__init__()
        self.is_even = False
        self.count_to_right_of_median = None

    def find_median_sorted_arrays(
            self, nums1: list[int], nums2: list[int]) -> float:
        sum_len = len(nums1) + len(nums2)

        if sum_len % 2 == 0:
            self.is_even = True
            self.count_to_right_of_median = (sum_len - 2) // 2
        else:
            self.is_even = False
            self.count_to_right_of_median = (sum_len - 1) // 2

        if len(nums1) == 0:
            return self.process_if_one_blank(nums2)
        if len(nums2) == 0:
            return self.process_if_one_blank(nums1)

        if nums2[0] >= nums1[-1]:
            return self.process_if_two_sorted(nums1, nums2)
        if nums1[0] >= nums2[-1]:
            return self.process_if_two_sorted(nums2, nums1)

        return self.search_in_nums(nums1, nums2)

    def process_if_two_sorted(
            self, small_nums: list[int], big_nums: list[int]) -> float:
        """
        Помогает искать, если оба списка отсортированны по отношению
        друг к другу

        Например:
        nums1: [1, 2, 3]
        nums2: [4, 5, 6]
        """

        if self.count_to_right_of_median < len(small_nums):
            # Если медиана лежит в первом(меньшем) массиве.
            result = small_nums[self.count_to_right_of_median]
            if self.is_even:
                # Если четное множество, то надо найти и второе число.
                # Оно все еще может быть в любом из массивов.
                if self.count_to_right_of_median + 1 < len(small_nums):
                    result += small_nums[self.count_to_right_of_median + 1]
                else:
                    result += big_nums[0]
                result /= 2
        else:
            # Если медиана в большем.
            right_mediana = len(big_nums) - self.count_to_right_of_median - 1
            result = big_nums[right_mediana]
            if self.is_even:
                # Для четных тут легко, раз мы и так уже во втором,
                # то просто берем предыдущее число
                result += big_nums[right_mediana - 1]
                result /= 2
        return float(result)

    def process_if_one_blank(self, nums: list[int]) -> float:
        """
        Помогает искать в одном массиве. Такое может произойти,
        если один из массивов был пустой.
        Тогда мы просто берем медиану второго.
        """
        result = nums[self.count_to_right_of_median]
        if self.is_even:
            result += nums[self.count_to_right_of_median + 1]
            result /= 2
        return result

    def search_in_nums(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Ищет через бин поиск по num1 число, которое бы являлось медианой.
        Если не нашло, то разворачивает поиск и запускает еще раз.
        """
        middle_p = 0
        right_p = len(nums1) - 1
        if len(nums1) <= self.count_to_right_of_median:
            left_p = 0
        else:
            left_p = right_p - self.count_to_right_of_median

        while left_p <= right_p:
            # ищем серединку в первом множестве
            middle_p = (left_p + right_p) // 2

            # что бы меньше букв дальше писать
            midle_v = nums1[middle_p]

            # считаем сколько нам не хватает справа
            miss_on_right = (
                self.count_to_right_of_median - len(nums1) + 1 + middle_p)

            if miss_on_right > len(nums2):
                # если нам не хватает больше, чем есть во втором,
                # то и искать нечего.
                # двигаем правый в середину.
                right_p = middle_p - 1
                continue

            if miss_on_right == 0:
                # краевой случай. Мы в первом множестве взяли самое левое
                # значение и ему всего достаточно. Осталось проверить,
                # что оно любого из второго множества
                if nums2[-1] <= midle_v:
                    # Оказалось больше ? Формируем ответ.
                    if self.is_even:
                        result = 0
                        if nums2[-1] > nums1[middle_p - 1]:
                            result = nums2[-1]
                        else:
                            result = nums1[middle_p - 1]
                        return (result + midle_v) / 2
                    return float(midle_v)
                left_p = middle_p + 1
                continue

            if nums2[len(nums2) - miss_on_right] >= midle_v:
                # Если серединка оказалась меньше или
                # равна числа правее места вставки.
                if len(nums2) - miss_on_right == 0 or nums2[
                        len(nums2) - miss_on_right - 1] <= midle_v:
                    # Если и предыдущее число меньше, то мы нашли ответ.
                    # Осталось его сформировать.
                    return self.get_answer(
                        nums1, nums2, middle_p, miss_on_right)

                left_p = middle_p + 1
            else:
                right_p = middle_p - 1

        return self.search_in_nums(nums2, nums1)

    def get_answer(
            self,
            nums1: list[int],
            nums2: list[int],
            right_mediana_i: int,
            miss_on_right: int) -> float:
        # Вспомогательная ф-ция. Помогает определить ответ.
        # right_mediana - Это уже найденная правая медиана в nums1.
        # Необходимо понять какая левая.
        if self.is_even:
            result = 0
            if right_mediana_i == 0:
                return (nums1[right_mediana_i] + nums2[
                    len(nums2) - miss_on_right - 1]) / 2

            if len(nums2) - miss_on_right - 1 < 0:
                m_sum = nums1[right_mediana_i] + nums1[right_mediana_i - 1]
                return (m_sum) / 2

            nums2_lv = nums2[len(nums2) - miss_on_right - 1]
            if nums2_lv > nums1[right_mediana_i - 1]:
                result = nums2[len(nums2) - miss_on_right - 1]
            else:
                result = nums1[right_mediana_i - 1]

            return (result + nums1[right_mediana_i]) / 2

        return float(nums1[right_mediana_i])

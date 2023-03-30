class Solution:
    def majority_element(self, nums: list[int]) -> int:
        first = second = 0
        first_counter = second_counter = 0

        for num in nums:
            if first == num:
                first_counter += 1
            elif second == num:
                second_counter += 1
            elif second_counter > first_counter:
                first_counter = 1
                first = num
            else:
                second_counter = 1
                second = num

        return first if first_counter > second_counter else second

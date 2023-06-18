from copy import deepcopy


class Solution:
    def minimum_total(self, triangle: list[list[int]]) -> int:
        result_counter = deepcopy(triangle[-1])

        for row_index in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[row_index])):
                left_child = result_counter[i]
                right_child = result_counter[i + 1]
                min_child = min(left_child, right_child)
                current_element = triangle[row_index][i]
                result_counter[i] = current_element + min_child
        return result_counter[0]

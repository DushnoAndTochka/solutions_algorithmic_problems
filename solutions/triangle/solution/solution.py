class Solution:
    def minimum_total(self, triangle: list[list[int]]) -> int:
        for row_num in range(1, len(triangle)):
            for element_index in range(len(triangle[row_num])):
                if element_index == 0:
                    left_prev_elem = triangle[row_num - 1][0]
                    triangle[row_num][element_index] += left_prev_elem
                elif element_index == len(triangle[row_num]) - 1:
                    right_prev_elem = triangle[row_num - 1][-1]
                    triangle[row_num][element_index] += right_prev_elem
                else:
                    triangle[row_num][element_index] += min(
                        triangle[row_num - 1][element_index - 1],
                        triangle[row_num - 1][element_index],
                    )

        return min(triangle[-1])

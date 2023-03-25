from typing import List


class Solution(object):

    def spiral_matrix(self, n: int, m: int) -> List[List[int]]:
        res = []
        # Ищем середину
        # TODO после исправления перестало работать... Исправить!
        # max_val_row_pos = n // 2
        max_val_col_pos = m // 2

        for row_num in range(n):
            new_row = []
            for col_num in range(m):
                # Сложное и не очень красивое условие,
                # которое позволяет определить, что мы в верхнем треугольнике.
                # См. текст выше
                is_up_tringle = (
                    (col_num + 1 >= row_num)
                    and (col_num <= m - row_num - 1)
                )
                if is_up_tringle:
                    # Расчет делается через "слои".
                    # каждый слой начинается с числа на 1 больше,
                    # чем закончился предыдущий.
                    # Более подробно можно почитать в solution/README.md
                    sq = n * m
                    first_in_lvl = (n - 2 * row_num) * (m - 2 * row_num)
                    new_row.append(sq - first_in_lvl + 1 + col_num - row_num)
                elif col_num <= max_val_col_pos and col_num <= n - row_num - 1:
                    # Левый треугольник. Все его числа на 1 меньше,
                    # чем число которое над ним
                    new_row.append(res[row_num - 1][col_num] - 1)
                elif col_num > max_val_col_pos and m - col_num <= n - row_num:
                    # Правый треугольник. Все его числа на 1 больше,
                    # чем число над ним
                    new_row.append(res[row_num - 1][col_num] + 1)
                else:
                    # Треугольник снизу. Все его числа на 1 меньше,
                    # чем число перед ним
                    new_row.append(new_row[-1] - 1)
            res.append(new_row)

        return res

    @staticmethod
    def print_result(result: List[List[int]]) -> None:
        """Вспомогательная ф-ция. Помогает красиво выводить ответ."""

        for row in result:
            for i, num in enumerate(row):
                num_str = str(num)
                row[i] = (4 - len(num_str)) * " " + num_str
            print(*i)

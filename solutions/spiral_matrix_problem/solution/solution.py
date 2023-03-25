from typing import List


class Solution(object):

    def spiral_matrix(self, n: int, m: int) -> List[List[int]]:
        res = []
        # Создаем матрицу и заполняем ее нулями. так как работаем по периметру,
        #   то нам необходимо подготовить весь массив перед заполнением
        for _ in range(n):
            new_l = [0] * m
            res.append(new_l)

        # считаем плозадь всего прямоугольника(кол-во всех элементов в матрице)
        count_all_numbers = n * m

        def filling_layer(layer=0):
            """
            Ф-циф, которая будет заполнять матрицу по слоям
            """
            # считаем какое кол-во колонок и строк на данном слое
            column_count = m - layer * 2
            row_count = n - layer * 2
            # находим число с которого начинается данный слой
            current_count_numbers = row_count * column_count
            current_num = count_all_numbers - current_count_numbers + 1

            # заполняем всю верхушку, кроме последнего символа
            for i in range(column_count - 1):
                res[layer][layer + i] = current_num
                current_num += 1

            # заполняем весь правый ряд, кроме последнего символа
            for i in range(row_count - 1):
                res[layer + i][layer + column_count - 1] = current_num
                current_num += 1

            # заполняем низ, кроме последнего
            for i in range(column_count - 1):
                row_i = layer + row_count - 1
                col_i = layer + column_count - 1 - i
                res[row_i][col_i] = current_num
                current_num += 1

            # заполняем левый край, кроме последнего.
            # Он у нас уже заполнен и равен начальному.
            for i in range(row_count - 1):
                res[layer + row_count - 1 - i][layer] = current_num
                current_num += 1

            # Если текущий размер матрицы больше чем 2 по обеим из сторон,
            # то мы еще не закончили.
            if column_count > 2 and row_count > 2:
                # увеличиваем слой и спускаемся ниже
                filling_layer(layer + 1)

        filling_layer()

        return res

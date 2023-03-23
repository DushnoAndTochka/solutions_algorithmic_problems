
class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        # Начальная высота 0
        c = m = 0

        for i in gain:
            # Каждую итерацию находим прибавляем разницу высот
            c += i
            # И обновляем максимум
            m = max(m, c)
        # Возвращаем результат
        return m

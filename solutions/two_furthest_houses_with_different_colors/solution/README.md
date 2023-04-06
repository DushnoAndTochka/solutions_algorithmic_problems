# Two Furthest Houses With Different Colors

Первое решение которое приходит в голову это пройтись сравнить каждый элемент с каждым и найти максимальное

```python
class Solution:
    def max_distance(self, colors: list[int]) -> int:
        result = 0
        length = len(colors)
        for i, color in enumerate(colors):
            for j in range(i, length):
                if color != colors[j]:
                    result = max(result, j - i)
        return result
```
Оценка по времени данного решения - O(N^2), а по памяти - константное.


Но можно улучшить решение, если найти самый дальний элемент от первого или самый дальний элемент от последнего

И это и будет ответ и данное решение будет работать за линейное время без использования линейной памяти

```python
class Solution:
    def max_distance(self, colors: list[int]) -> int:
        # Инициализирует результат нулём
        result = 0
        length = len(colors)
        first = colors[0]
        last = colors[-1]
        # Проходимся по всем элементам и
        # если элемент не совпадает с первым или последним
        # то обновляем максимум
        for i, color in enumerate(colors):
            if color != first:
                result = max(result, i)
            if color != last:
                result = max(result, length - 1 - i)
        return result
```

# 1502. Can Make Arithmetic Progression From Sequence

Первое что приходит в голову это отсортировать и проверить 
что каждый элемент отличается на одинаковое количество от предыдущего

```python
class Solution:
    def can_make_arithmetic_progression(self, arr: list[int]) -> bool:
        # Если меньше двух точек то возвращаем True
        if len(arr) <= 2:
            return True
        
        # Сортируем
        arr.sort()
        # Берём итератор
        it = iter(arr)
        # Первый элемент
        first = next(it)
        # Второй элемент
        previous = next(it)
        # Находим разницу
        diff = previous - first

        for item in it:
            # Сравниваем разницу, если не равно то возвращаем False
            if item - previous != diff:
                return False
            # Меняем предыдущий элемент
            previous = item
        # Возвращаем True
        return True
```

Такое решение работает за O(N*logN) и не использует линейную дополнительную память

Но можно использовать дополнительную память и увеличить время работы алгоритма.

Можно найти найти минимальное и максимальное число

После этого найти какая должная быть разница между каждым элементом

И после этого проверить каждый элемент в массиве, если все присутствуют, то возвращаем True


```python
class Solution:
    def can_make_arithmetic_progression(self, arr: list[int]) -> bool:
        # Если меньше двух точек то возвращаем True
        if len(arr) <= 2:
            return True

        # Находим максимальный элемент и минимальный
        max_ = max(arr)
        min_ = min(arr)
        # Находим разницу, которая должная быть
        diff = (max_ - min_) / (len(arr) - 1)
        
        # Если разница не целочисленная, то возвращаем False
        # Так как у нас только целые числа
        if diff != diff // 1:
            return False

        diff //= 1
        
        # Если все элементы равны друг другу, возвращаем True
        if diff == 0:
            return True
        
        # Находим только уникальные элементы
        unique = set(arr)
        
        # Если есть повторы, то возвращаем False
        if len(arr) != len(unique):
            return False

        # Проверяем что все элементы арифметической прогрессии присутствуют в массиве

        current = min_
        for _ in range(len(arr) - 1):
            current += diff
            if current not in unique:
                return False

        return True
```

У нас получилось время работы по времени O(N) и по памяти O(N).

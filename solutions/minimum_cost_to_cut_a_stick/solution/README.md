# Minimum Cost to Cut a Stick Problem


Для решения данной задачи, необходимо перебрать все варианты и выбрать минимально возможный.

И можно это сделать следующий образом.

```python
import itertools


class Solution:

    def min_cost(self, n: int, cuts: list[int]) -> int:
        
        # Получаем отсортированные индексы разрезов
        cuts = sorted(itertools.chain(cuts, [0, n]))

        # Функция получения цены разреза от left до right
        def get_cost(left: int, right: int):
            # Если левый и правый отличается меньше чем на единицу, то цена 0 
            if right - left == 1:
                return 0
            # Находим разницу между левым и правым
            length = cuts[right] - cuts[left]
            
            costs = []
            # Находим все цены разрезов, если мы будем разрезать в любом месте
            for i in range(left + 1, right):
                costs.append(get_cost(left, i) + get_cost(i, right))
            # Берем минимальный и добавляем длину текущего отрезка
            return min(costs) + length
        # Находим цену всего отрезка
        return get_cost(0, len(cuts) - 1)
```

Но как мы можем догадаться, функция get_cost будет вызываться много раз с одними и теми же аргументами.

Поэтому лучше ее кешировать, а для этого можно воспользоваться декоратором `functools.cache`

И итоговое решение получается такое

```python
import functools
import itertools


class Solution:

    def min_cost(self, n: int, cuts: list[int]) -> int:
        
        # Получаем отсортированные индексы разрезов
        cuts = sorted(itertools.chain(cuts, [0, n]))

        # Функция получения цены разреза от left до right
        @functools.cache
        def get_cost(left: int, right: int):
            # Если левый и правый отличается меньше чем на единицу, то цена 0 
            if right - left == 1:
                return 0
            # Находим разницу между левым и правым
            length = cuts[right] - cuts[left]
            
            costs = []
            # Находим все цены разрезов, если мы будем разрезать в любом месте
            for i in range(left + 1, right):
                costs.append(get_cost(left, i) + get_cost(i, right))
            # Берем минимальный и добавляем длину текущего отрезка
            return min(costs) + length
        # Находим цену всего отрезка
        return get_cost(0, len(cuts) - 1)
```

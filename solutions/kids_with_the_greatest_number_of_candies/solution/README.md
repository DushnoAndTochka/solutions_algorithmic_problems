# KidsWithTheGreatestNumberOfCandies Problem

Первое что приходит в голову, это создать цикл и проходить по каждому элементу.

Для каждого элемента проверять меньше ли сумма элемента и дополнительных конфет каждого из элементов, если да, то для этого элемента возвращаем False, иначе True.


```python

class Solution:
    
    def kids_with_candies(self, candies: list[int], extra: int) -> list[bool]:
        r = []
        
        for i in candies:
            updated = i + extra
            
            for j in candies:
                if j > updated:
                    r.append(False)
                    break
            else:
                r.append(True)
            
        return r
```

Теперь попробуем найти сложность данного алгоритма.

Для каждого элемента мы проходимся по всему массиву - поэтому сложность по скорости будет O(N^2).

Мы создаем один массив длина которого равно длине исходного массива - поэтому сложность по памяти будет O(N).

Данное решение работает долго и его можно улучшить, если заметить то что мы сравниваем updated со всеми, но можем сравнить с максимальным за вычетом extra, который мы расчитываем предварительно. 

То есть будет вот такое решение

```python

class Solution:

    def kids_with_candies(self, candies: list[int], extra: int) -> list[bool]:
        # Находим максимум за вычетом extra
        m = max(candies) - extra
        # Создаем масссив True/False для каждого элемента
        return [i >= m for i in candies]
```

# 228. Summary Ranges

Здесь решение сразу приходит в голову, идём от первого элемента и 
дальше и если прошлый элемент не равен previous+1, то у нас будет один range. 

Но здесь нужно аккуратно всё расписать


И первая функция, которая нам понадобится, эта функция которая 
превращает начало и конец в строку

```python
def to_str(start, end):
    return f'{start}->{end}' if start != end else str(start)
```

А теперь и само решение

```python
import itertools

def to_str(start, end):
    return f'{start}->{end}' if start != end else str(start)

class Solution:
    def summary_ranges(self, nums: list[int]) -> list[str]:
        # Если пустой массив, то возвращаем так же пустой массив
        if not nums:
            return []
        # Берём первый элемент и присваиваем, ему и начало и конец
        end = start = nums[0]
        # Инициализируем результат
        result = []
        # Проходимся по всем элементам начиная со второго элемента
        # Тут обращаю внимание, что это эквивалентно
        # nums[1:] - только nums[1:] копирует список, а itertools.islice 
        # просто проходит по существующему 
        for num in itertools.islice(nums, 1, len(nums)):
            # Если текущий элемент не равен предыдущий + 1 
            if num != end + 1:
                # То добавляем в результат range
                result.append(to_str(start, end))
                # И обновляем start
                start = num
            # Обновляем end всегда
            end = num
        # Добавляем последний range в результат
        result.append(to_str(start, end))
        # И возвращаем результат
        return result
```

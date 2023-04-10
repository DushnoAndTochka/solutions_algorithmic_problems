# Boats to Save People

Так как в лодке может быть максимум 2 человека, мы можем использовать жадный алгоритм.

Отсортировать массив и после этого брать человека с самым большим весом и отправлять его с человеком с самым маленьким весом, можно поместить 2 человека в лодку.

То есть если у нас такой массив

```python
people = [3,2,2,1]
limit = 5
```

Сначала сортируем массив

```python
people = [1,2,2,3]
```

В первую лодку помещаем элемент справа
.
И пробуем поместить второй элемент и берём его слева.

Но 3 + 1 > 4, поэтому берём только один элемент справа.

```python
people = [1,2,2]
```

Теперь у нас такой массив и проделываем тоже самое.

Берем 2 и 1 -> сумма не больше 3, поэтому берем оба элемента

Остается такой массив
```python
people = [2]
```

И один элемент помещаем в массив

То есть решение с использованием deque вот такое будет

```python
import collections


class Solution:
    def num_rescue_boats(self, people: list[int], limit: int) -> int:
        # Сортируем
        people.sort()
        # Получаем deque из отсортированного массива
        d = collections.deque(people)
        # Инициализируем результат нулём
        r = 0
        while len(d) >= 2:
            # Удаляем правый элемент
            i = d.pop()
            # Если сумма не больше лимита, то удаляем и левый
            if d[0] + i <= limit:
                d.popleft()
                
            # Добавляем 1 к результату
            r += 1
        # Если у нас в массиве остался один элемент, то он поедет в отдельной лодке
        r += len(d)
        return r
```

Но здесь сразу можно заменить небольшую оптимизацию, мы можем не использовать deque, а держать 2 указателя на элементы 

То есть решение будет вот таким

```python

class Solution:
    def num_rescue_boats(self, people: list[int], limit: int) -> int:
        # Сортируем
        people.sort()
        # Левый указатель
        left = 0
        # Правый указатель
        right = len(people) - 1
        result = 0
        # Идем до тех пор пока разница больше либо равна 1
        while right - left >= 1:
            # Если сумма не превышаем лимит, то левый двигаем
            if people[left] + people[right] <= limit:
                left += 1
            # Правый двигаем всегда
            right -= 1
            # Добавляем 1 к результату
            result += 1
            
        # Если один элемент остался, то добавляем 1 к результату
        if left == right:
            result += 1

        return result
```

Решение как можно заменить работает за O(NlogN) - так как тут самая долгая операция это сортировка.

По памяти решение использует константную память - O(1).
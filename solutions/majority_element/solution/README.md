# Majority Element

Можно пройтись по словарю и найти частоту каждого элемента. После этого найти элемент который встречается больше всего

### Как это выглядит ?

```python

class Solution:
    def majority_element(self, nums: list[int]) -> int:
        # Инициализиуем мапу
        m = {}
        
        # Проходимся по всем элементам мапу
        for num in nums:
            # Если элемента в мапе нет, то ставим 0
            m.setdefault(num, 0)
            # Добавляем 1
            m[num] += 1
        r = nums[0]
        max_counter = m[r]
        
        # Находим максимум в мапе
        for item, counter in m.items():
            if max_counter < counter:
                max_counter = counter
                r = item
        return r
```

Данное решение работает за линейное время и используем линейную память

Так же данное решение можно переписать с использованием Counter



```python
import collections

class Solution:
    def majority_element(self, nums: list[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]
```

Но можно увидеть, что мы не используем одно условие, которое нам дается в задаче - нам надо найти не элемент, который встречается чаще всего, а элемент, частота которого больше 50%.

А в таком случае, можно не создавать мапу и не держать частоту всех элементов, можно поддерживать частоту только двух элементов и вернуть максимум.

Ниже представлено решение

```python
class Solution:
    def majority_element(self, nums: list[int]) -> int:
        # Два элемента, инициализиуем любым числом
        first = second = 0
        # Говорим что оба элемента встречались уже 0 раз, что является правдой
        first_counter = second_counter = 0

        # Проходимся по всем элементам
        for num in nums:
            # Если равно первому, то просто увеличиваем счетчик для первого
            if first == num:
                first_counter += 1
            # Если равно второму, то просто увеличиваем счетчик для второго
            elif second == num:
                second_counter += 1
            
            # Если это новое число, то заменяем меньшее на него
            elif second_counter > first_counter:
                first_counter = 1
                first = num
            else:
                second_counter = 1
                second = num
        # Возвращаем число с наибольшим счетчиком
        return first if first_counter > second_counter else second
```

В данном решении мы используем константную память и
проходимся по всем элементам один раз (то есть O(n) по времени и O(1) по памяти).

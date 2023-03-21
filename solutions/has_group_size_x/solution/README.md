# X of a Kind in a Deck of Cards

## Описание:
Данную задачу можно решить следующим образом

 - Найти количество дубликатов для каждого элемента
 - Найти наибольший общий делитель всех этих чисел
 - Если НОД больше 1, то возвращает True иначе False

Данное решение будет использовать линейную дополнительную память O(n)

И будет работать за линейное время O(n)

### Вспомогательные функции

Вычисления НОД списка чисел в python

```python
import math

items = [5,10, 45]
# HOД - Greatest common divisor
assert math.gcd(*items) == 5
```

Так же рекомендую посмотреть пакет math (там есть и НОК и много чего еще)

### Возможное решение

```python
import collections
import math

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        # Получаем словарь из списка - [1,2,3,1] -> {1: 2, 2: 1, 3: 1}
        # Ключ словаря - это элемент списка, а значение - количество элементов в списке
        d = collections.Counter(deck)

        # Начинаем итерироваться по значениям
        values = iter(d.values())
        # Берем первое значение
        # Мы можем не проверять на то что первого значения нет,
        # deck имеет длину >= 1
        gcd = next(values)

        # Итерируемся по всем значениям
        for value in values:
            # Находим НОК двух чисел
            gcd = math.gcd(gcd, value)

            # Если НОК равен 1, то значит минимальная группа - это 1 и на группы,
            # в которых больше 1го элемента мы разбить не можем
            if gcd == 1:
                return False
        # Если НОК всех чисел больше 1
        # То разбить на группы можно
        return gcd > 1
```

### Упрощение кода

Функция math.gcd - может принимать больше двух значений


```python
import collections
import math

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        d = collections.Counter(deck)
        values = d.values()
        # Используем распаковку, для передачи всех значений values
        # в функцию math.gcd
        return math.gcd(*values) > 1
```

### Решение в одну строчку

```python
import collections
import math

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        return math.gcd(*collections.Counter(deck).values()) > 1
```

### Дополнение

Возможное нахождение НОД без использования math

```python
def gcd(a, b):
    # После выхода из цикла, один из элементов 0
    while a != 0 and b != 0:
        # Внутри цикла присваиваем большему числу, 
        # остаток от деления большего числа на меньшее
        if a > b:
            a = a % b
        else:
            b = b % a
    # Возвращаем не нулевой элемент
    # (Сумма числа + 0 будет само число, поэтому можно просуммировать)
    return a + b
```

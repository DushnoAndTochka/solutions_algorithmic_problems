# 1286. Iterator for Combination

В Python обычно данный функционал реализуют через генератор, а не через функцию,
поэтому можно написать класс, который использует генератор, а после будет разбирать уже как написать функцию

```python

# Наш генератор
def combinations(characters: str, combinationLength: int):
    ...


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        # Инициализируем генератор
        self._it = combinations(characters, combinationLength)
        # Это для следующего значения
        self._next = None

    def next(self) -> str:
        # Если следующее значение есть, то возвращаем его
        if self._next is not None:
            result = self._next
            self._next = None
            return result
        # Если нет, то возвращаем следующее значение из генератора
        return next(self._it)

    def hasNext(self) -> bool:
        # Если есть следующее значение, то возвращает True
        if self._next is not None:
            return True
        # Если нет, то берём из генератора
        try:
            self._next = next(self._it)
        except StopIteration:
            return False
        return True
```

Данный класс ничего особенного не делает, это просто обортка над генератором

А теперь остановится на том, как же можно написать генератор

И самый простой способ, это использовать itertools

```python
import itertools


def combinations(characters: str, combinationLength: int):
    for item in itertools.combinations(characters, combinationLength):
        # В itertools возвращается tuple, а нам нужна строка, 
        # поэтому просто меняем формат
        yield ''.join(item)
```


А как же можно написать свой генератор

```python

# Я полностью скопировал с https://docs.python.org/3/library/itertools.html#itertools.combinations
# Но немного изменил возвращаемое значение
def combinations(pool, r):
    n = len(pool)
    
    if r > n:
        return
    # Начальные индексы - [0, 1, 2,  ...]
    indices = list(range(r))
    # Возвращаем первое значение
    yield ''.join(pool[i] for i in indices)
    while True:
        # Находим индекс с конца, который можно увеличить
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            # Выходим из функции, если дошли до конца цикла
            return
        # Увеличиваем индекс
        indices[i] += 1
        for j in range(i+1, r):
            # Увеличиваем все индексы, начиная с i+1 и до конца
            indices[j] = indices[j-1] + 1
        # Возвращаем значение
        yield ''.join(pool[i] for i in indices)
```


А теперь резберём работу алгоритма на примере ABCD и 3

У нас инициализиуется indices = [0, 1, 2]

Поэтому первое возвращаемое значение будет ABC

После этого мы находим индекс, который можно увеличить и это будет 2

И увеличиваем его и теперь indices = [0, 1, 3]

И теперь возвращаем значение ABD

Теперь находим индекс, который можно увеличить и это будет 1

Увеличиваем индекс и теперь получаем indices = [0, 2, 3]

И возвращаем значение ACD

Теперь опять ищем индекс, который мы можем увеличить и это уже будет 0

Увеличиваем индекс и получаем [1, 2, 3]

И теперь возвращаем значение BCD

И после этого уже выходим из цикла

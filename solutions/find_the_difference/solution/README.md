#  Find the Difference Solution

## Описание:

### Решение через dict:
Кажется самое очевидное решение этой задачи. Сначала мы считаем все символы строки `s`, потом начинаем вычитать все символы строки `t`, если встретили уникальный или какой-то символ ушел в отрицательное кол-во, то мы нашли.

```python
class Solution:
    def find_the_difference(self, s: str, t: str) -> str:
        char_count = defaultdict(int)

        for c in s:
            # считаем все символы первой строки
            hash_m[c] += 1

        for c in t:
            if c not in hash_m:
                # уникальный символ == ответ
                return c
            
            hash_m[c] -= 1
            if hash_m[c] < 0:
                # символ встретился больше раз,
                # чем в первой строке == ответ
                return c
```

### Решение через ord:
Решение уже посложнее, так как подразумевает, что вы знакомы с ord ф-цией. Она преобразует "буквы" в байтовое представление(в `int`). Если у нас всего 1 символ уникальный, значит разница сумм даст нам ответ.

```python
class Solution:
    def find_the_difference(self, s: str, t: str) -> str:
        result = 0

        for i in s:
            # тут символов меньше,
            # значит лучше вычитать
            result -= ord(i)

        for i in t:
            # прибавляем и тем
            # самым убираем одинаковые символы
            result += ord(i)

        # преобразуем обратно в символ
        return chr(result)
```

### Решение через ord + XoR:
Ну и вытекающее решение из предыдущего. Если вы знакомы с XoR, то предыдущее вообще покажется вам странным. Про XoR уже писал и не раз

> Можно почитать [тут](/solutions/single_number/solution/README.md).

```python
class Solution:
    def find_the_difference(self, s: str, t: str) -> str:
        result = 0

        for i in s:
            result ^= ord(i)

        for i in t:
            result ^= ord(i)

        return chr(result)
```
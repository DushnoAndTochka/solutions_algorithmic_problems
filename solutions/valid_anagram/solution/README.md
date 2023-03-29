# ValidAnagram Solution

## Описание

Данная задача имеет множетсво решений. Рассмотрим несколько из них.

### Решение через `HashMap`(`Dict`)

Наверное самое наивное решение. Мы создадим словарь и будем запоминать сколько раз встретили ту или иную букву первого слова. Потом для пторого слова произведем обратную операцию, то есть мы будем отнимать у каждой буквы `1`. Итогом у нас долен получиться словарь, у которого все `value` равны `0`.

```python
class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        hash_m = defaultdict(int)
        
        # Если длина разная, то и проверять нечего.
        if len(s) != len(t):
            return False

        # складываем и вычитаем за один проход.
        for i in range(len(s)):
            hash_m[s[i]] += 1
            hash_m[t[i]] -= 1

        # смотрим нет ли "значения", которое отлично от 0
        for v in hash_m.values():
            if v != 0:
                return False

        return True
```

Более короткая закпись того же решения

```python
import collections


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
```

Делает по сути тоже самое. Только коротко и относительно быстро.

### Решение через `ord` и `XOR`

Во первых у нас известно, что все буквы в слове латинские и в нижнем регистре. Так же мы знаем, что у букв есть числовое представление через таблицу ASCII. Мы уже разбирали `XOR`(single_number задача). Почему бы нам не сложить все числовые представления букв через `XOR` ?

Но есть проблема... Строка `aa` и `bb` для такого подхода эквиваленты...

Что делать ? 

Можно помимо этого, считать еще и сумму `ord` этих строк, после сравнить и если равны по `XOR` и `sum(ords)`, то все ок. Правда ? Нет...

`ad == cb` при такой истории.

Что теперь ?
А что если четные прибавлять, а неченые вычетать. Тогда мы закроем все проблемы, описанные выше.

```python
class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        counter_t = counter_s = counter_xor = 0

        first_char_ord = ord('a')

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            ord_s = ord(s[i]) - first_char_ord
            ord_t = ord(t[i]) - first_char_ord
            counter_xor ^= ord_s ^ ord_t

            if ord_s % 2 == 0:
                counter_s += ord_s
            else:
                counter_s -= ord_s
            
            if ord_t % 2 == 0:
                counter_t += ord_t
            else:
                counter_t -= ord_t

        return counter_xor == 0 and counter_s == counter_t
```

Решение больше фановое, чем серьезное. Но само по себе интересное.


### Решение на `алфавите`.

Решение собирающее идеи из предыдущих. Мы поняли что в первом круто и быстро можно искать. во втором вспомнили, что букву, можно представить как число, а зная значение первой буквы, сделать отсчет с `0`.

В таком случае нам ничего не мешает создать список и работать с ним через индексы.

```python
class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        first_char_ord = ord('a')

        alph = [0] * 26
        for i in range(len(s)):
            alph[ord(s[i]) - first_char_ord] += 1
            alph[ord(t[i]) - first_char_ord] -= 1

        for i in alph:
            if i != 0:
                return False

        return True
```
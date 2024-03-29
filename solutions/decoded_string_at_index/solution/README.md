# Decoded String at Index Solution

## Описание:

Давайте для начала поймем что от нас требует сама задача, без этого придумать решение достаточно сложно.

У нас есть некая сжатая строка, необходимо развернуть ее по правилам и сказать какая буква находится на `k`-ом месте(не идексе, это важно).

Давайте начнем с простого


```python
s = "ab2c3d"
k = 12

res_s = "ababcababcababcd"
res = "b"
```

Можно попробовать развернуть строку, но это ОЧЕНЬ дорого и долго. Во первых строки являются неихменяемым типом в питоне и каждый раз мы будем создавать новую строку. Во вторых это не всегда вообще необходимо.

```python
s = "a999"
k = 1

res_s = "a" * 9 ** 3
res = "a"
```

Умножать можно устать, а ответ изначально был понятен...

Как же такие ситуации обыгрывать ? Начнем с первого, что стоит заметить. Нам нет нуждды иметь всю итоговую строку, а только ту, длинна которой меньше, либо равна `k`.

```python
s = "a999"
k = 2

res_s = "aaaaaaaaa"
res = "a"
```

Те мы должны получить строчку, по правилам преобразования, что бы ее длина покрывала наше `k`.

Но и этого будет не достаточно, если мы собираемся все еще складывать строки... Значит стоит заметить что-то еще.

Заметить стоит повторяемость тех или иных действий

```python
s = 'ab2c3d'
k = 12

# a -> 1
# ab -> 2
# abab -> 4
# ababc -> 5
# ababcababcababc -> 15
# ababcababcababcd -> 16

res_s = "ababcababcababcd"
res = "b"
```

Мы уже поняли, что стоит останавливаться на длине, которая больше или равна `k`, теперь пора придумать как начать искать в обратную сторону. Посомтрев пример выше, станет понятно, что строки `ababcababcababc` достаточно для поиска 12 элемента, так как он в ней гарантированно есть и там ничего нового не появится. Теперь давайте поймем что это за строка вообще.

`"ababcababcababc" == "ababc" + "ababc" + "ababc"`

Те строка состоит из 3-х строк и это легко понять по множителю из исходной, сжатой, строки. Нам нужен 12 символ. В первой из трех подстрок его не будет, там только 5 символов, во второй так же не будет, там еще 5 символов и не больше. Значит нам нужен 2 символ из третьей подстроки. На что похоже ??? На остаток от деления конечно.

Теперь у нас есть строка `"ababc"` и нам нужен ее второй символ. Уже сильно легче найти его глазами ? А теперь давайте и эту длину уменьшим, что бы стало понятно по изначальной строке, что это за символ. Выкинем `c` он точно лишний. `"abab"` получим такое. Все еще больше чем хотелось бы. Давайте уменьшим в два раза(это обратное действие к изначальной строке). Получим `ab`. И вот теперь мы легко ответим, что второй символ это `b`. 

Что же напоминает данное решение ? Это чистой воды стэк. Мы можем запоминать длину строки, которая будет в тот или иной момент `развертывания` и принимать решения отталкиваясь от этих данных


```python
class Solution:
    def decode_at_index(self, s: str, k: int) -> str:
        # тут будем хранить текущую
        # длину развертывания
        result = [0]

        for c in s:
            if c.isdigit():
                # встретили число ? 
                # Умножаем последнюю длину на него
                result.append(result[-1] * int(c))
            else:
                # Встретили букву ? 
                # Увеличиваем на 1 
                # относительная предыдущей длинны
                result.append(result[-1] + 1)

            if result[-1] >= k:
                # длина стала больше k ?
                # Мы нашли Диапозон поиска
                break

        for i in range(len(result) - 1, -1, -1):
            if result[i] > k:
                # длина больше k ?
                # Значит забиваем и идем дальше
                continue
            
            # Так как длины и символы лежат на одних
            # и тех же индекса с учетом сдвига в 1
            # (так как в длиннах была нулевая длина),
            # то мы легко можем понять какой символ
            # из изначальной строки мы сейчас 
            # обрабатываем в обратном порядке
            c = s[i - 1]
            if result[i] == k:
                # длинна и k совпали ?
                # мы либо нашли ответ, либо должны
                # разделить на число и продолжить
                # поиск
                if c.isdigit():
                    k //= int(c)
                    continue
                return c

            # длина меньше k ?
            # значит пора посмотреть где именно
            # лежит наше число.
            if k % result[i] != 0:
                k = k % result[i]
                continue
            if c.isdigit():
                k //= int(c)
                continue
            return c
```

В данном примере решение непосредственно через массив. Так наглядней и не приходится ничего пересчитывать в обратном направлении. Но есть отличное, которое построенно на константе по памяти

```python
class Solution:
    def decode_at_index(self, s: str, k: int) -> str:
        l = 0
        i = 0
        
        while l < k:
            if s[i].isdigit():
                l *= int(s[i])
            else:
                l += 1
            i += 1
        
        for j in range(i-1, -1, -1):
            char = s[j]
            if char.isdigit():
                l //= int(char)
                k %= l
                continue
            if k == 0 or k == l:
                return char
            l -= 1
```

Почище выглядит. Идея точно такая же, протсо мы в обратную сторону пересчитываем все значения, которые храним в массиве в первом решении. 
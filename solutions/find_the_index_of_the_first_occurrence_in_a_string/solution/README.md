#  Find the Index of the First Occurrence in a String Solution

## Описание:

Решение не содержит каких-либо хитростей. Мы итерируемся по строке `haystack` и ищем символ, который равен первому символу из строки `needle`. Как только нашли, то смотрим, что бы все остальные символы так же были одинаковы, если это так, то возвращаем индекс первого символа. Если нет, то возвращаемся к поиску первого символа их `needle` в `haystack` и повторяем все до конца строки.

```python
class Solution:
    def str_str(self, haystack, needle):
        # пошли по строке haystack
        # Ее длину сразу уменьшаем. Это необходимо для случая,
        # когда вся строка needle лежит в конце haystack.
        # Наприме:
        # needle, haystack = sss, aasss
        # В таком случае нам надо понять насколько
        # вообще целесообразно сравнивать хвост
        # от haystack и весь needle
        for i in range(len(haystack) - len(needle) + 1):
            # первые символы равны ? Сравниваем остальные
            if haystack[i] == needle[0]:
                # сравниваем остальные
                for j in range(len(needle)):
                    if haystack[i + j] != needle[j]:
                        break
                else:
                    # break не пустит нас в этот блок
                    return i
        # ничего не смогли найти
        return -1
```
# Decoded String at Index Problem

## Описание:

Дана строка `s` и число `k`. Она состоит из букв и цифр. Необходимо преобразовать строку и вернуть символ с индексом `k` из преобразованной строки. Способ преобразования:
- Если встретили букву, то просто ее оставляем
- Если встретили цифру, то умножаемм текущую строку на это число.

## Пример:

```python
s = 'as2fg2'
k = 3

# as (2) == asas
# asas + fg (2) == asasfgasasfg
s_changed = 'asasfgasasfg'

result = 's' # s_changed[3]
```

---

<a href="https://leetcode.com/problems/decoded-string-at-index/">Задача на LeetCode</a>

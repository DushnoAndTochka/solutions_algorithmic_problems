# Zigzag Conversion Problem

## Описание:

На вход подается строка `s` и число `numRows`. Строка `s` должна быть представленна в виде зигзагообразной записи в `numRows` строк. Как это выглядит ?  Например у нас есть строка `PAYPALISHIRING` и `numRows=3`, тогда запись можно представить следующим образом:

```
P   A   H   N
A P L S I I G
Y   I   R

# представим в виде индексов символов

0     4     8    12
1  3  5  7  9  11
2     6     10
```

После этого необходимо склеить строки и вернуть результат `PAHN + APLSIIG + YIR == PAHNAPLSIIGYIR`

## Пример:

```python
s = "PAYPALISHIRING"
numRows = 4

result = "PINALSIGYAHRPI"
```

---

<a href="https://leetcode.com/problems/zigzag-conversion/">Задача на LeetCode</a>
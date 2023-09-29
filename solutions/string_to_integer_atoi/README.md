# String to Integer (atoi) Problem

## Описание

Необходимо написать ф-цию, которая преобразует строку в 32-ух разрядное число по следующим правилам:

- читаем и игнорируем все начальные пробелы
- учитывать символ `+` или `-`, он показывает знак результирующега числа. Если знак не указан, то считаем результат положительным числом.
- Читаем строку до конца или до первого не числового символа.(не считая знаки из пункта выше)
- Если число выходит за диапозон 32-ух разрядных чисел `[-2**31, 2**31 - 1]`, то берем по ближайшей границе(`"2**34" -> 2**31`). Если числа нет, то возвращаем 0


## Пример:

```python
s = "42"

result = 42
```

```python
s = "   -3451Any word"

result = -3451
```

---

<a href="https://leetcode.com/problems/string-to-integer-atoi/">Задача на LeetCode</a>
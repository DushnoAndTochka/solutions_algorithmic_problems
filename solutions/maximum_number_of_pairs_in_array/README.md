# Maximum Number of Pairs in Array Problem

## Описание

На вход дается массив целых чисел. Необходимо попарно удалить одинаковые числа и вернуть следующее `[pair_count, alone_count]`, где

- pair_count - кол-во пар, которые были удалены.
- alone_count - кол-во чисел, которые остались и не нашли свою пару.

## Пример:

```python
nums = [1, 3, 2, 1, 3, 2, 2]
```

На первом шаге мы удалилим пару однерок. Получим массив

```python
nums = [3, 2, 3, 2, 2]
```

Теперь мы можем удалить пару троек и получим массив

```python
nums = [2, 2, 2]
```

Теперь удалим пару двоек и получим массив

```python
nums = [2]
```

Больше удалять нечего. Ответ будет `[3, 1]`, так как мы удалили `3-и` пары чисел, а в остатке осталось `одно` число

---
<a href="https://leetcode.com/problems/maximum-number-of-pairs-in-array/">Задача на LeetCode</a>
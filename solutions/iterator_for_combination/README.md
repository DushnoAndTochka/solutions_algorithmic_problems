# 1286. Iterator for Combination

Разработайте класс `CombinationIterator`:

`CombinationIterator(string characters, int combinationLength)` -  данный класс инициализируется с помощью строковых символов, состоящих из отсортированных отдельных строчных букв латинского алфавита и числового значения `comboLength` в качестве аргументов.
next()  - возвращает следующую комбинацию длин `comboLength` в лексикографическом порядке.
hasNext() Возвращает `true` тогда и только тогда, когда существует следующая комбинация.


### Пример 
```python
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]

# output
[None, "ab", True, "ac", True, "bc", True]

# Explanation
it = CombinationIterator("abc", 2)
it.next()    # return "ab"
it.hasNext() # return True
it.next()    # return "ac"
it.hasNext() # return True
it.next()    # return "bc"
it.hasNext() # return False
```

---
<a href="https://leetcode.com/problems/iterator-for-combination/">Задача на LeetCode</a>
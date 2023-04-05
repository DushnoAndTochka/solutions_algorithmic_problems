# TopKFrequentWords Problem

## Описание
На вход подается массив строк и число `k`. Необходимо вернуть `k` самых популярных слов в этом массиве.

Популярность определятся по кол-ву повторения этого слова в массиве. Если кол-во повторений одинаковое, то дофильтровываем по алфавиту(`лексикографически`).

## Пример

```python
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
```

В примере видно, что 2-мя самыми популярными, являются слова `["i",  "love"]`. Кол-во их повторений равно, поэтому они дофильтрованы по алфавиту.

---
<a href="https://leetcode.com/problems/top-k-frequent-words/">Задача на LeetCode</a>
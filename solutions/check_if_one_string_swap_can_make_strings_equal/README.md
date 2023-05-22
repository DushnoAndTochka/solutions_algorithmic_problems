# Check if One String Swap Can Make Strings Equal

Даны две строки s1 и s2 одинаковой длины. 

Обмен строками — это операция, при которой вы выбираете два индекса в строке (не обязательно разных) и меняет местами символы в этих индексах.

Нужно вернуть True, если можно сделать обе строки равными, выполнив не более одной замены строк ровно на одной из строк. 

В противном случае вернуть False.



### Привет 1.

```python

s1 = "bank"
s2 = "kanb"

result = True
```

Можно поменять местами первый символ с последним символом s2, чтобы получилось «bank».

### Пример 2.

```python
s1 = "attack"
s2 = "defend"

result = False
```

### Пример 3.

```python

s1 = "kelb"
s2 = "kelb"

result = True
```

---
<a href="https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/">Задача на LeetCode</a>

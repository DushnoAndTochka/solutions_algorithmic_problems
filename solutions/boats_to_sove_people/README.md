# Boats to Save People

## Описание:
Имеется массив people, где people[i] - это размер i-го человека.

Так же есть неограниченное количество лодок, которые могут перевести максимум 2 человека и вес не больше limit.

Нужно вернуть минимальное количество лодок, необходимое для того что бы перевести всех людей.

### Пример 1:
```python
people = [1,2]
limit = 3

result = 1 # Одна лодка (1, 2)
...
```

### Пример 2:

```python
people = [3,2,2,1]
limit = 3

result = 3 # Три лодки (1, 2), (2) и (3)
```

### Пример 3:

```python
people = [3,5,3,4]
limit = 5

result = 4 # 4 лодки (3), (3), (4), (5)
```

---
<a href="https://leetcode.com/problems/boats-to-save-people/">Задача на LeetCode</a>
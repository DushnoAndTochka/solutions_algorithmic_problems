# Unique Paths II Problem

> Задача является продолжением, более сложной версией, к задаче [Unique Paths](/solutions/unique_paths/)

## Описание

Как и в оригинальной задаче, нам дается поле. В левом верхнем углу стоит робот. Финишь находится в нижнем правом углу. Необходимо посчитать кол-во вариантов, которыми робот может дойти до финиша. Робот может шагать либо вправо, либо вниз.

НО добавляются препятствия на пути. Робот не может ходить по таким клеткам. 

Пример:

```
obstacle_grid = [[0,0,0],[0,1,0],[0,0,0]]

|---|---|---|
| R | 0 | 0 |
|---|---|---|
| 0 | 1 | 0 |
|---|---|---|
| 0 | 0 | F |
|---|---|---|

result = 2
```

Путей в таком случае всего `2`. Либо по верхней грани, либо по нижней.

---
<a href="https://leetcode.com/problems/unique-paths-ii/">Задача на LeetCode</a>
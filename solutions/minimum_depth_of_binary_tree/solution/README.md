# Minimum Depth of Binary Tree Solution

## Описание

Задача на DFS или BFS. Нам необходимо пройтись по дереву и найти `самую близкую` конечную ноду. 

### DFS
DFS в данной задаче уже в самом начале выглядит более проигрышной, так как заставляет нас спускаться до самого низа по веткам, которые могут быть не самыми удачными. Поэтому нам прийдется пройтись по всем веткам и выбрать минимальную, то есть мы гарантированно всегда будем иметь сложность `O(n)`, где `n` это кол-во нод в дереве.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
            
        def dfs(node, current_dist):
            # Так как кол-во нод не превышает этого значения
            # по условия, то мы возьмем его как максимально
            # возможное
            left_m = right_m = 10**5
            if node.left:
                # пошли по левой ветке
                left_m = dfs(node.left, current_dist + 1)
            if node.right:
                # пошли по правой
                right_m = dfs(node.right, current_dist + 1)
            if node.right is None and node.left is None:
                # дошли до конечного узла. вернем что насчитали
                return current_dist
            # вернем минимум из результатов левой и правой веток
            return min(left_m, right_m)

        return dfs(root, 1)
```

Это не самый оптимальный код и далеко не самый лаконичный. НО он хорошо отражает суть всех действий. Мы идем по левому краю, пока это возможно, потом начинаем подниматься и пробовать сходить в правый узел. И так далее, пока не пройдем ВСЕ узлы. 

### BFS

Решение через BFS выглядит куда лучше. Нам не прийдется делать лишних походов. Мы пройдем ровно столько `уровней`, сколько необходимо для нахождения ответа и не пойдем ниже. В худшем случае сложность все так же составит `O(n)`, ведь нам прийдется пройти все узлы до последнего. НО если ответ находится не на самом низком уровне, то мы найдем его достаточно быстро и уж точно быстрее чем при DFS.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # узлы которые мы хотим посетить и их уровень
        nodes = [(root, 1)]

        for node, lvl in nodes:
            # закончились варианты спуска ?
            # Значит ответ найден
            if node.left is None and node.right is None:
                return lvl

            if node.left:
                nodes.append((node.left, lvl + 1))
            if node.right:
                nodes.append((node.right, lvl + 1))

        return nodes[-1][1]
```

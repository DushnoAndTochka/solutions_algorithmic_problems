# Minimum Absolute Difference in BST Solution

## Описание

Сама задача кажется изначально запутанной. Поэтому предлагаю распутывать ее постепенно. Для начала необходимо понять, что вообще от нас хотят.

Нам дается корень бинарного дерева поиска. Необходимо найти минимальную разницу между двумя любыми его вершинами.

### Решение через bfs:
На первый взгляд работать с деревом очень не удобно в данной задаче, поэтму можно развернуть дерево в список и уже работать с ним.

```
        root

          |
          V

          4
         / \
        2   6
       / \ 
      1   3
```
Преобрахуем данное дерево в список пройдясь `bfs` и получим `[4, 2, 6, 1, 3]`. Теперь можно было бы начать искать два заветных числа, но и тут загвостка. Прийдется каждое число повычитать с каждым. Это займет `O(n^2)`. Выглядит долго. Тогда можно понять, что минимальную разницу дадут такие два числа, которые находятся максимально рядом на исловой прямой, то есть нет смысла из `6` вычитать `1`, так как есть `2` и она гарантиравонно даст меньшую разницу с любым из этих чисел. Я кланю к сортировки, она займет не больше чем O(n * log(n)) и вот уже после этого имеет смысл искать разницы между парами.

После сортировки получим

```
[1, 2, 3, 4, 6]
```

Тут уже все совсем просто. Начинаем искать попарную разницу и выбираем минимальную из них.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_minimum_difference(self, root: Optional[TreeNode]) -> int:
        sorted_values = [root]
        bfs_nodes = []

        for node in bfs_nodes:
            bfs_nodes.append(node.val)
            if sorted_values.left is not None:
                sorted_values.append(node)
            
            if sorted_values.right is not None:
                sorted_values.append(node)

        sorted_values.sort()

        result = sorted_values[-1]

        for i in range(1, len(sorted_values)):
            result = min(
                result, sorted_values[i] - sorted_values[i - 1]
                )

        return result
```
Итоговая сложность O(n * log(n)).

Решение выглядит дико не оптимальным. Так что давайте еще подумаем.

### Решение через dfs:

Пора вспомнить описание задачи. По нему говорилось, что нам дается дерево поиска. А какими св-ми обладает дерево поиска ?

> - оба поддерева — левое и правое — являются двоичными деревьями поиска;
> - у всех узлов левого поддерева произвольного узла X значения ключей >  данных меньше либо равны, нежели значение ключа данных самого узла X;
> - у всех узлов правого поддерева произвольного узла X значения ключей данных больше, нежели значение ключа данных самого узла X.
> 
> Более подробно можно почитать [на wiki.](https://ru.wikipedia.org/wiki/Двоичное_дерево_поиска)

Что нам это дает ? Это дает тот факт, чот у нас уже все отсортированно. Значит нам не надо даже заморачиваться на этот счет. Если мы будем двигаться всегда в лево, то найдем самое маленькое значение в этом дереве. Ничего не напоминает ? верно, тут отлично подойдет dfs и спуск по левой стороне. Тогда мы сразу получим отсортированный список.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sorted_values = []

        def sorting_node_values(node):
            if node.left is not None:
                sorting_node_values(node.left)
            sorted_values.append(node.val)
            if node.right is not None:
                sorting_node_values(node.right)

        sorting_node_values(root)
        result = sorting_node_values[-1]

        for i in range(1, len(sorted_values)):
            result = min(result, sorted_values[i] - sorted_values[i - 1])

        return result
```

Итоговая сложность O(n).
Решение уже выглядит куда лучше. Но кажется оно так же может быть улучшенно.

### Оптимизированное решение через dfs.

В предыдущем решении мы используем массив, для хранения значения всех нод, потом проходимся по ним в поисках минимальной разницы, но при этом значения мы добавляем последовательно одну за одной и получаем сразу отсортированный список. Зачем нам вообще хранить целый массив, если можно просто хранить значение предыдущго значения и текущего ? Правильно, не за чем. Мы прям на ходу будем искать результат.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_minimum_difference(self, root: Optional[TreeNode]) -> int:
        # по условию никакое число в дереве не превышает 100001.
        # Значит возьмем его.
        self.result = 100001
        self.prev_value = None

        def sorting_node_values(node):
            if node.left is not None:
                sorting_node_values(node.left)

            if self.prev_value is not None:
                self.result = min(self.result, node.val - self.prev_value)
            self.prev_value = node.val

            if node.right is not None:
                sorting_node_values(node.right)

        sorting_node_values(root)

        return self.result
```

Итоговая сложность O(n). А по памяти у нас константа.
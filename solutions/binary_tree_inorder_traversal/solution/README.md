# Binary Tree Inorder Traversal

Сначала нужно понять что такое inorder обход.

Для обхода дерева нужно:
- Вернуть все элементы из левого дерева (в таком же порядка)
- Вернуть корень дерева
- Вернуть все элементы правого ребенка (в таком же порядка)

### Рекурсивное решение

```python

# Функция обхода дерева
def inorder_traversal(node):
    # Если нода None, то ничего возвращать не нужно
    if node is None:
        return
    # Сначала возвращаем все элементы из левого ребенка
    yield from inorder_traversal(node.left)
    # Возвращаем саму ноду
    yield node
    # Возвращаем все элементы из правого ребенка
    yield from inorder_traversal(node.right)


class Solution:
    def inorder_traversal(self, root) -> list[int]:
        # Возвращаем только значения нод
        return [node.val for node in inorder_traversal(root)]
```

Рекурсивное решение делает прям то как мы и описали в определении


### Решение с использованием цикла

```python
class Solution:
    def inorder_traversal(self, root) -> list[int]:
        # Инициализируем результат
        result = []
        # Инициализируем стек
        stack = []
        # Берем текущий элемент
        current = root

        while True:
            # Если текущий элемент не None значит добавляем его в stack и переходим к его левому ребенку
            # Так как мы используем стек мы будет получать элементы в обратном порядке
            # а это как раз то что нам нужно
            if current is not None:
                stack.append(current)
                current = current.left
            # Если стек не пустой
            elif stack:
                # Получаем элемент стека 
                # Так как мы получили элемент стека, то значит слева мы уже прошли все элементы
                # добавляем элемент в результат и после ставим текущий элемент в правого ребенка
                current = stack.pop()
                result.append(current.val)
                current = current.right
            else:
                # Если текущий элемент None и stack пустой, то значит мы обошли все элементы
                break
        # Возвращаем результат
        return result
```

### Сложность алгоритма

Оба алгоритма работают за линейное время с использованием линейной памяти.
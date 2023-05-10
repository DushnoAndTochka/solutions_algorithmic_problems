# Flatten Binary Tree to Linked List

Для решения задачи намного нужно обойти в правильном порядке ноды и изменить их.


Есть 2 стандартных способа обхода дерева через рекурсию или использую цикл

### Решение с использованием цикла 
И начнем с обхода циклом

```python
class Solution:
    def flatten(self, root) -> None:
        # Если нам передали пустое дерево, то делать ничего не будем
        if root is None:
            return None
        
        # Инициализируем stack
        stack = []
        # Запоминаем предыдуший элемент
        prev = root
        
        # Добавляем в stack правого и левого ребенка
        self._add_from_node(stack, root)
        
        # Итерируемся до тех пор пока stack не пуст
        while stack:
            # Достаем последний добавленный элемент
            # Если у предыдущего элемента был левый элемент, то это будет он
            node = stack.pop()
            
            # Проставляем следующий элемент у предыдущего
            prev.right = node
            # Ставим left в None - так нужно по условию
            prev.left = None
            # Добавляем детей текущего элемента
            self._add_from_node(stack, node)
            # Обновляем предыдущий элемент
            prev = node
        # Не забываем обновить left у последнего элемента
        prev.left = None

    def _add_from_node(self, stack, node):
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

```

Данное решение использует дополнительную линейную память (stack) и работает за линейное время (нужно обойти все элементы).

### Решение рекурсией

А теперь разберем рекурсивное решиние

```python

# Функция возвращает генератор, который обходим все элементы в правильном порядке
def walk(node):
    # Если None пришел то ничего возвращать не нужно
    if node is None:
        return
    
    # Сначала получаем left, right так так их обновляем
    left = node.left
    right = node.right
    # Возвращаем ноду
    yield node
    # Затем возвращаем все ноды из левого ребенка - рекурсивный вызов
    yield from walk(left)
    # Затем возвращаем все ноды из правого ребенка - рекурсивный вызов
    yield from walk(right)


class Solution:
    def flatten(self, root) -> None:
        # Если нам передали пустое дерево, то делать ничего не будем
        if root is None:
            return None
        # Получаем генератор
        it = walk(root)
        # Получаем первый элемент
        current = next(it)
        # Проходимся по всем элементам в генераторе 
        for next_ in it:
            # Проставляем у текущего элемента следующий
            current.right = next_
            #  left в None - по условию
            current.left = None
            # Обновляем текущий элемент
            current = next_

```

Здесь нет никаких массивов и может показаться что тут не используется линейная память, но это не так так как мы используем рекурсию - а рекурсия увеличивает стёк и получается что у нас может быть на стеке линейная память.

### Решение без использования дополнительной памяти
 
```python
class Solution:
    def flatten(self, root):
        # Получаем текущий элемент
        current = root
        # Пока текущий элемент не None продолжаем цикл
        while current is not None:
            # Если у элемента есть левый ребенок
            if current.left is not None:
                
                # Левый ребенок будет предыдущим элементом
                previous = current.left
                # Если у предыдущего элемента есть правый ребенок
                # То делаем его предыдущим
                while previous.right is not None:
                    previous = previous.right
                
                # Ставим у предыдущего элемента следующий 
                previous.right = current.right
                # Меняем правого и левого соседа
                current.right = current.left
                # Ставим left в None по условию
                current.left = None
            # Переходим к следующему элементу
            current = current.right
```

А вот как работает данное решение

```


       1                     1                       1
      / \                     \                       \
     /   \                     2(left->right)          2
    2     5      ---->        / \          --->         \
   / \     \                 /   \                       3(left->right) 
  3   4     6               3     4                       \
                                   \                       4  - Элементы ниже не изменились
                                    5                       \
                                     \                       5
                                      6                       \
                                                               6
```

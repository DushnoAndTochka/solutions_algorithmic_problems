# Same Tree

Первое решение которое может прийти в голову это использовать рекурсию

- Сравнить элементы
- Рекурсивно сравнить левых детей
- Рекурсивно сравнить правых детей

А вот и реализация на Python

```python
class Solution:
    def is_same_tree(self, p, q) -> bool:
        
        # Если один из них None, то возвращаем результат
        if p is None or q is None:
            return q == p
        # Если элементы не равны, то возвращаем False
        if p.val != q.val:
            return False
        
        # Вызываем рекурсивно сравниние для левых и правых детей
        return self.is_same_tree(p.right, q.right) and self.is_same_tree(p.left, q.left)
```

Но помимо рекурсивного решения есть и обход дерева нерекурсивный

```python
import collections

class Solution:
    def is_same_tree(self, p, q) -> bool:
        # Инициализируем очередь
        queue = collections.deque()
        
        queue.append((p, q))      
        
        # Идём по циклу пока очередь не пуста
        while queue:
            
            # Достаем элементы
            p_child, q_child = queue.popleft()

            # Если оба None, то переходим к следующему
            if p_child is None and q_child is None:
                continue
            
            # Если один None, а другой нет, то возвращаем False
            if p_child is None or q_child is None:
                return False
            
            # Если значений не равны, то возвращаем False
            if p_child.val != q_child.val:
                return False
            
            # Кладём левых детей
            queue.append((p_child.left, q_child.left))
            
            # Кладём правых детей
            queue.append((p_child.right, q_child.right))

        return True
```

Оба решения работают за линейное время и с использованием линейной памяти.

В рекурсивном алгоритме, мы используем память на стеке, а во втором решении мы используем queue. 

Так же во втором решении можно было использовать простой список вместо collections.deque.

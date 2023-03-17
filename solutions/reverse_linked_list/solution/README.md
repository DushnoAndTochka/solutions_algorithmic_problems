# ReverseLinkedList Solution

## Описание идеи
Мы просто перебрасываем указатели на каждом элементе. Для этого нам необходимо помнить текущий, предыдущий и следующий. Текущий мы отправляем на предыдущий и запоминаем его как предыдущий. 

## Как это выглдит ?

```
          curr   next
LinkedList: 1  ->  2  ->  3  ->  4  ->  ...  ->  n  ->  None

Answer: None
        prev
```
### Шаг 1

```
          curr   next
LinkedList: 1      2  ->  3  ->  4  ->  ...  ->  n  ->  None
            
            |
            V

Answer:   None
          prev
```
### Шаг 2

```
                  curr   next
LinkedList:        2      3  ->  4  ->  ...  ->  n  ->  None
            
                   |
                   V

Answer:  None  <-  1
                 prev
```

### Шаг 3

```
                        curr   next
LinkedList:               3     4  ->  ...  ->  n  ->  None
            
                          |
                          V

Answer:  None  <-  1  <-  2
                        prev
```

### Шаг n

```
                                               curr    next
LinkedList:                                      n     None
            
                                                 |
                                                 V

Answer:  None  <-  1  <-  2  <-  3  <-  ...  <-  n-1
                                          prev
```


## Решение на python

```python
from typing import Optional

def reverseList(head: Optional['ListNode']) -> Optional['ListNode']:
    prev = None # Первый элемент должен ссылаться на None
    curr = head
    
    # Будем двигаться по всем элементам и менять им next 
    while curr is not None:
        # Запоминаем следующий элемент, позже он будет curr    
        next_ = curr.next 
        # Ставим текущему элементу ссылку на предыдущее
        curr.next = prev 
        # Ставим текущий элемент, как предыдущий
        prev = curr
        # А следующий как текущий
        curr = next_
        
    # Возвращаем имеено prev так как curr это None
    # Если head==None, то prev тоже None, 
    # то есть обрабатывать специально None не нужно 
    return prev
```
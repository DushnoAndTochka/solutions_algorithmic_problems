# Add Two Numbers II Solution

## Описание:

Начнем с решения через стэк.
Мы можем сложить все ноды в стэк и начать выдерать ноды с конца, аккуратно складывая их и создавая новые связи. После чего добить, если оказалось, что одна из нод была более длинной.

Решение будет выглядить очень страшно:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        l2_list = []

        # начинаем разрывать изначальные ноды
        # и помещать в соответствующие стэки.
        # Не забываем порвать старые связи,
        # что бы потом не мучаться
        while l1 is not None:
            l1_list.append(l1)
            prev_l1 = l1
            l1 = l1.next
            prev_l1.next = None
        
        while l2 is not None:
            l2_list.append(l2)
            prev_l2 = l2
            l2 = l2.next
            prev_l2.next = None

        # голова от состояния None будет
        # подниматься все выше и выше
        head = None
        # переменная в которой будет
        # хранить потенциальную единицу в "уме"
        member = 0
        while l1_list and l2_list:
            # выдергиваем из стэка ноды
            l1 = l1_list.pop()
            l2 = l2_list.pop()
            # нам нет разницы какую из нод брать,
            # так как в данном цикле мы пройдемся
            # только на равную длину
            l1.next = head
            head = l1

            # складываем, не забывая про "в уме"
            head.val = l1.val + l2.val + member
            member = 0
            if head.val >= 10:
                member = 1
                head.val -= 10

        while l1_list:
            # осталось что-то в первом стэке ?
            # добиваем
            l1 = l1_list.pop()
            l1.next = head
            head = l1

            head.val += member
            member = 0
            if head.val >= 10:
                member = 1
                head.val -= 10

        while l2_list:
            # осталось что-то во втором стэке ?
            # добиваем
            l2 = l2_list.pop()
            l2.next = head
            head = l2

            head.val += member
            member = 0
            if head.val >= 10:
                member = 1
                head.val -= 10

        if member:
            # получилось так что кол-во элементов равное,
            # но что то осталось в уме ? создаем доп ноду
            # Пример: 5 + 5
            node = ListNode(1, head)
            head = node

        return head
```

Решение в целом нормальное. Мы пройдемся по всем нодам суммарно дважды. Первый раз когда создаем стэк, второй раз когда этот стэк читаем. Память тоже терпима. Но можно и лучше, если схитрить

Что Если не создавать никакого стэка, а формировать сразу число с домножением его десятков

```
1 -> 2 -> 3

EQ

((1) * 10 + 2) * 10 + 3 == 123
```

Таким образом мы можем легко получить именно итоговые числа. сложить их уже будет совсем легко. останется получить результат. Тут нам поможет возможность сконвертить `int` в `str` и создать новый связанный список. Решение так же не идеально, но чуть хитрее предыдущего


```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        sum2 = 0

        # преобразуем исходные связанные списки в числа
        while l1:
            sum1 = (sum1 * 10) + l1.val
            l1 = l1.next
        while l2:
            sum2 = (sum2 * 10) + l2.val
            l2 = l2.next
        
        # складываем и превращаем в строку
        sm = str(sum1 + sum2)
        # начинаем формировать итоговый связанный список
        node = head = ListNode(sm[0])
        for i in range(1, len(sm)):
            node.next = ListNode(sm[i])
            node = node.next

        return head
```

Решение сильно короче и читается полегче. Но сказать что оно прям на голову лучше, я не могу
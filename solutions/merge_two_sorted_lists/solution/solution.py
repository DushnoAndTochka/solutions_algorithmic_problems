from __future__ import annotations


class ListNode(object):
    """Узел односвязанного списка."""

    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next


class Solution(object):
    
    def merge_two_sorted_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # создаем рузельтирующую голову
        head = ListNode()
        # Переменная указывающая на последнбб отсортированнуб ноду.
        current_node = head

        # цикл, который работает сразу с двумя списками
        while list1 is not None and list2 is not None:
            
            if list2.val > list1.val:
                # Если значение в первом меньше чем в втором,
                # значит мы к результату прилинковываем эту нод
                # и переходим к следующей.
                current_node.next = list1
                list1 = list1.next
            else:
                # Обратное к предыдущему.
                current_node.next = list2
                list2 = list2.next

            # Так как мы отсортировали уже следующую ноду, мы переходим к ней.
            current_node = current_node.next

        if list1 is not None:
            current_node.next = list1
        else:
            current_node.next = list2

        # не забываем, что HEAD указывает на пустышку. 
        # нас интересует следующая за ним нода.
        return head.next
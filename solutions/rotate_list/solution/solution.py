from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotate_right(
            self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # суммарно необхоимо три указателя.
        # head - изначальная голова
        # last_node - последняя нода
        # new_head - место будущего разрыва
        new_head = last_node = head

        # ищем реальную длину связанного списка
        len_ll = 0
        while last_node:
            last_node = last_node.next
            len_ll += 1

        if len_ll < 2:
            # значит менять нечего
            return head

        # делаем k меньше длины списка
        # помним что если связанный список повернуть k раз,
        # где k равен длине связанного списка, то мы получим
        # изначальный список.
        k = k - len_ll * (k // len_ll)

        if k == 0:
            # значит менять нечего
            return head

        last_node = head

        while last_node.next:
            # ищем место разрыва
            last_node = last_node.next

            if k:
                k -= 1
            else:
                new_head = new_head.next

        # производим замыкание связанного списка и
        # его последующий разрыв, но уже в новом месте
        last_node.next = head
        head: ListNode = new_head.next
        new_head.next = None

        return head

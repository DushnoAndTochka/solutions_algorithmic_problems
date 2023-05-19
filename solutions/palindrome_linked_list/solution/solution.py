from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            # нет смоысла такое проверять.
            # Обработаем как краевой случай.
            return True

        # ищем длину связанного списка
        len_ll = 1
        node = head
        while node.next:
            node = node.next
            len_ll += 1

        mid = len_ll // 2

        # разворачиваем первую половина связанного списка
        left_node = right_node = head
        for i in range(mid - 1):
            next_right = right_node.next
            right_node.next = next_right.next

            next_right.next = left_node
            left_node = next_right

        # смещаем указатель с середины на первую ноду правой половины
        right_node = right_node.next
        if len_ll % 2 != 0:
            right_node = right_node.next

        # сравниваем развернутую первую половину,
        # с оригинальной правой.
        for i in range(mid):
            if left_node.val != right_node.val:
                return False
            left_node = left_node.next
            right_node = right_node.next

        return True

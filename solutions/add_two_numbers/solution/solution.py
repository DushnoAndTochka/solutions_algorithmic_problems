from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:

    def add_two_numbers(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]) -> Optional[ListNode]:
        # создаем голову результирующего списка
        result_head = result = ListNode()
        # переменная для "держать в уме"
        member_num = 0

        # пока хотя бы одна нода не закончена, мы идем
        while l1 is not None or l2 is not None:
            # переменная в которой будет результат суммы двух нод,
            # с учетом числа, что мы запомнил с прошлой операции.
            next_val = member_num

            if l1 is not None:
                # если l1 доступна, берем значение и
                # двигаемся по листу дальше
                next_val += l1.val
                l1 = l1.next

            if l2 is not None:
                # если l2 доступен, берем значение и
                # двигаемся по листу дальше
                next_val += l2.val
                l2 = l2.next

            # если мы насчитали больше 10,
            # значит единицу надо перенести в следующий разряд
            if next_val >= 10:
                member_num = 1
                next_val -= 10
            else:
                member_num = 0

            # складываем то что насчитали в следующую
            # ноду в результирующем линкед листе
            result.next = ListNode(val=next_val)
            result = result.next

        if member_num:
            # может получиться так, что два числа в сумме дают число,
            # которое больше чем они по разряду, не стоит этого забывать.
            # Пример: 9 + 1 = 10
            result.next = ListNode(val=1)

        return result_head.next

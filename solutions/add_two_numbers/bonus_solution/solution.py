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
        # Считаем что первый список является результируеющем.
        # Выставляем на него все необходимые указатели.
        # result - то что улетит из ф-ции как ответ
        # current_result_node - нода которую мы модифицировали последней
        result = current_result_node = l1
        # делаем себе якорь на случай, если окажется
        # что l2 более длинный список.
        l2_result = l2

        member_num = 0

        while l1 is not None or l2 is not None:
            next_val = member_num

            if l1 is not None:
                next_val += l1.val

            if l2 is not None:
                next_val += l2.val

            if next_val >= 10:
                member_num = 1
                next_val -= 10
            else:
                member_num = 0
            # До этих пор все шло как и предыдущем решении.
            # Только мы l1 и l2 не переключали дальше.

            if l1 is None:
                # Если у нас закончились ноды в l1 списке,
                # значит мы будем работать с l2 и
                # результат переключим на l2,
                # так как он оказался более длинным
                current_result_node = l2
                result = l2_result
                l2.val = next_val
                l2 = l2.next
            elif l2 is None:
                # ровно наоборот, только якорь нам не нужен,
                # получается что мы и так угадали с выбором.
                current_result_node = l1
                l1.val = next_val
                l1 = l1.next
            else:
                # если оба списка еще не закончились, то работаем с ними.
                current_result_node = l1
                l2.val = next_val
                l2 = l2.next
                l1.val = next_val
                l1 = l1.next

        if member_num:
            current_result_node.next = ListNode(val=1)

        return result

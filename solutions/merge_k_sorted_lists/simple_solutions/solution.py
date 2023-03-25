from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution(object):
    def merge_k_lists(self, lists: Optional[ListNode]):

        nodes = []
        result = point = ListNode(0)
        for list in lists:
            # сваливаем все в один массив
            while list:
                nodes.append(list.val)
                list = list.next

        nodes.sort()  # сортируемся
        for value in nodes:
            # собираем уже отсортированные
            # данные в новый связанный список
            point.next = ListNode(value)
            point = point.next

        return result.next

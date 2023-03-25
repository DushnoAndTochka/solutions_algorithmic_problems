from __future__ import annotations

from heapq import heappop, heappush
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def merge_k_lists(
            self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values, head, pointer = [], None, None
        for node in lists:
            while node:
                # свваливаем все в одну кучу.
                heappush(values, node.val)
                node = node.next

        while values:
            # из кучи собираем ответ в обратном порядке.
            if head is None:
                head = ListNode(heappop(values))
                pointer = head

            else:
                pointer.next = ListNode(heappop(values))
                pointer = pointer.next

        return head

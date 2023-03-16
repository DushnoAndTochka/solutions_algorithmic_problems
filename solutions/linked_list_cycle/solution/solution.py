from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        bread_crumbs = 10 ** 5 + 1

        while head is not None:
            if head.val == bread_crumbs:
                return True
            
            head.val = bread_crumbs
            head = head.next
        
        return False

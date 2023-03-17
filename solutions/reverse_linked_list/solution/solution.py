from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int=0, next: Optional[ListNode]=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

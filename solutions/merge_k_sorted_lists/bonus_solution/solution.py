from __future__ import annotations
from heapq import heappop, heappush
from typing import Optional, List


class ListNode:
    def __init__(self, val: int=0, next: Optional[ListNode]=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self,lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values,head,pointer=[],None,None
        for l in lists:
            while l:
                # свваливаем все в одну кучу.
                heappush(values,l.val)
                l=l.next

        while values:
            # из кучи собираем ответ в обратном порядке.
            if head is None:
                head=ListNode(heappop(values))
                pointer=head

            else:
                pointer.next=ListNode(heappop(values))
                pointer=pointer.next

        return head 

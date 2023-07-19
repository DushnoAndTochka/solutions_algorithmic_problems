from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sum1 = 0
        sum2 = 0

        while l1:
            sum1 = (sum1 * 10) + l1.val
            l1 = l1.next
        while l2:
            sum2 = (sum2 * 10) + l2.val
            l2 = l2.next

        sm = str(sum1 + sum2)
        node = head = ListNode(sm[0])
        for i in range(1, len(sm)):
            node.next = ListNode(sm[i])
            node = node.next

        return head

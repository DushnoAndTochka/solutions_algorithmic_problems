from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(
            self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        node = uniq_node = head

        while node is not None:
            if node.val != uniq_node.val:
                uniq_node.next = node
                uniq_node = node
            node = node.next

        uniq_node.next = None

        return head

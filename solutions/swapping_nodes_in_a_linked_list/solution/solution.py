from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swap_nodes(
            self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = start_node = end_node = head

        counter = 1

        while node.next:
            node = node.next

            if counter < k:
                start_node = node
                counter += 1
            else:
                end_node = end_node.next

        start_node.val, end_node.val = end_node.val, start_node.val

        return head

from __future__ import annotations
from typing import Optional, List


class ListNode:
    def __init__(self, val: int=0, next: Optional[ListNode]=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_sorted_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """Код полностью скопирован из merge_two_sorted_lists solution."""
        head = ListNode()
        current_node = head

        while list1 is not None and list2 is not None:
            
            if list2.val > list1.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next

            current_node = current_node.next

        if list1 is not None:
            current_node.next = list1
        else:
            current_node.next = list2
            
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Принцип турнирной таблицы. Берем по два и получаем один,
        так до тех пор пока не закончатся пары. А если пары закончились,
        значит 'победитель' найден
        """
        
        if not lists:
            return None
            
        i = 0
        while i + 1 < len(lists):
            first_l = lists[i]
            i += 1
            second_l = lists[i]
            i += 1
            merged_list = self.merge_two_sorted_lists(first_l, second_l)
            lists.append(merged_list)

        return lists[-1]

import collections


class Solution:
    def buddy_strings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        goal_diff = None
        s_diff = None
        swapped = False
        for s_item, goal_item in zip(s, goal):
            if s_item == goal_item:
                continue
            if swapped:
                return False
            if goal_diff is None:
                goal_diff = goal_item
                s_diff = s_item
                continue
            if goal_diff != s_item or s_diff != goal_item:
                return False
            swapped = True
        if swapped:
            return True
        if goal_diff is not None:
            return False

        if len(s) > 26:
            return True
        return collections.Counter(s).most_common(1)[0][1] > 1

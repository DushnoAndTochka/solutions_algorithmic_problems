
class Solution:
    def can_make_arithmetic_progression(self, arr: list[int]) -> bool:
        if len(arr) <= 2:
            return True
        max_ = max(arr)
        min_ = min(arr)
        diff = (max_ - min_) / (len(arr) - 1)

        if diff != diff // 1:
            return False

        diff //= 1

        if diff == 0:
            return True

        unique = set(arr)

        if len(arr) != len(unique):
            return False

        current = min_
        for _ in range(len(arr) - 1):
            current += diff
            if current not in unique:
                return False

        return True

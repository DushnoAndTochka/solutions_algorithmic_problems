class Solution:
    def can_make_arithmetic_progression(self, arr: list[int]) -> bool:
        if len(arr) <= 2:
            return True

        arr.sort()
        it = iter(arr)
        first = next(it)
        previous = next(it)
        diff = previous - first

        for item in it:
            if item - previous != diff:
                return False
            previous = item
        return True

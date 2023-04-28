
class Solution:

    def reverse(self, x: int) -> int:
        result = 0
        is_negative = False
        if x < 0:
            is_negative = True
            x = -x

        max_ = 2147483647 // 10

        while x > 0:

            if result > max_:
                return 0

            result *= 10
            x, mod = divmod(x, 10)
            result += mod

        if is_negative:
            result = -result

        return result

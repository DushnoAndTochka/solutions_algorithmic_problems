class Solution:
    def my_pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if -1 > n or n > 1:
            next_n = n // 2

            if n % 2 != 0:
                x *= self.my_pow(x * x, next_n)
            else:
                x = self.my_pow(x * x, next_n)
        elif n == -1:
            x = 1 / x

        x: float
        return x

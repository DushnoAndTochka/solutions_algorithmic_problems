def guess(num: int, pick: int = 0) -> int:
    if num > pick:
        return -1

    if num < pick:
        return 1

    return 0


class Solution:
    def guess_number(self, n: int) -> int:
        # Как и в классическое задаче по бинпоиску,
        # выставляем границы
        left, rigth = 0, n

        while left <= rigth:
            mid = (left + rigth) // 2

            # берем середину и делаем предположение.
            current_guess = guess(mid)

            # if-ы один к одному как в условии задачи.
            if current_guess == 0:
                return mid

            if current_guess == 1:
                left = mid + 1
            else:
                rigth = mid - 1

        return -1

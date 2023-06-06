class Solution:
    def check_straight_line(self, coordinates: list[list[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        initialized = False
        a = b = c = 0
        it = iter(coordinates)

        x1, y1 = next(it)

        for x2, y2 in it:
            if x1 == x2 and y2 == y1:
                continue
            if not initialized:
                a = y1 - y2
                b = x2 - x1
                c = x1 * y2 - y1 * x2
                initialized = True
            elif a * x2 + b * y2 + c != 0:
                return False
        return True

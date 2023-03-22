pick: int

def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0
    

class Solution:
    def guessNumber(self, n: int) -> int:
        pass
    
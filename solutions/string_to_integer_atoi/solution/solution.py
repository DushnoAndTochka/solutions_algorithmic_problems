class Solution:
    def my_atoi(self, s: str) -> int:
        i = res = 0
        op = 1
        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s) and s[i] in "+-":
            op = 1 if s[i] == "+" else -1
            i += 1

        mres = (1 << 31) - 1 if op == 1 else 1 << 31
        while i < len(s) and s[i].isdigit() and res <= mres:
            res = res * 10 + int(s[i])
            i += 1

        return min(res, mres) * op

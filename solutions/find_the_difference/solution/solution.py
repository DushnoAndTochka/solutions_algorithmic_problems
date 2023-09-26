class Solution:
    def find_the_difference(self, s: str, t: str) -> str:
        result = 0

        for i in s:
            result ^= ord(i)

        for i in t:
            result ^= ord(i)

        return chr(result)

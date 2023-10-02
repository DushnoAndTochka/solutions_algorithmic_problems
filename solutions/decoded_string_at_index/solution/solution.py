class Solution:
    def decode_at_index(self, s: str, k: int) -> str:
        result = [0]

        for c in s:
            if c.isdigit():
                result.append(result[-1] * int(c))
            else:
                result.append(result[-1] + 1)

            if result[-1] >= k:
                break

        for i in range(len(result) - 1, -1, -1):
            if result[i] > k:
                continue

            c = s[i - 1]
            if result[i] == k:
                if c.isdigit():
                    k //= int(c)
                    continue
                return c

            if k % result[i] != 0:
                k = k % result[i]
                continue
            if c.isdigit():
                k //= int(c)
                continue
            return c

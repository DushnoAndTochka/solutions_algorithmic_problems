class Solution:
    def generate(self, num_rows: int) -> list[list[int]]:
        result = []

        for n in range(num_rows):
            row = [1]
            result.append(row)

            for m in range(1, n + 1):
                row.append(row[-1] * (n - m + 1) // m)

        return result

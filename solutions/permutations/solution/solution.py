class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = [[]]

        for num in nums:
            for i in range(len(result)):
                result[i].append(num)
                for j in range(len(result[i]) - 1):
                    res = []
                    for k in range(-1 - j, len(result[i]) - 1 - j):
                        res.append(result[i][k])
                    result.append(res)

        return result

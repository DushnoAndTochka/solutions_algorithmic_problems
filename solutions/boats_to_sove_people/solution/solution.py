class Solution:
    def num_rescue_boats(self, people: list[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        result = 0

        while right - left >= 1:

            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            result += 1

        if left == right:
            result += 1

        return result

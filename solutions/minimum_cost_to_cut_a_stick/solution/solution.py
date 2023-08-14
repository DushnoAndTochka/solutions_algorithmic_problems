import functools
import itertools


class Solution:

    def min_cost(self, n: int, cuts: list[int]) -> int:
        cuts = sorted(itertools.chain(cuts, [0, n]))

        @functools.cache
        def get_cost(left: int, right: int):
            if right - left == 1:
                return 0
            length = cuts[right] - cuts[left]

            costs = []
            for i in range(left + 1, right):
                costs.append(get_cost(left, i) + get_cost(i, right))
            return min(costs) + length

        return get_cost(0, len(cuts) - 1)

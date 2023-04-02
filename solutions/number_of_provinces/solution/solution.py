class DisjointSet:

    def __init__(self, n: int):
        self._parents = [i for i in range(n)]
        self._ranks = [0 for _ in range(n)]

    def find(self, i: int) -> int:
        if i != self._parents[i]:
            self._parents[i] = self.find(self._parents[i])
        return self._parents[i]

    def union(self, i: int, j: int):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self._ranks[i_id] > self._ranks[j_id]:
            self._parents[j_id] = i_id
        else:
            self._parents[i_id] = j_id
            if self._ranks[i_id] == self._ranks[j_id]:
                self._ranks[j_id] += 1


class Solution:
    def find_circle_num(self, is_connected: list[list[int]]) -> int:
        n = len(is_connected)
        s = DisjointSet(n)

        for i in range(n):
            for j in range(i + 1, n):
                if is_connected[i][j] == 1:
                    s.union(i, j)
        roots = set()
        for i in range(n):
            roots.add(s.find(i))
        return len(roots)

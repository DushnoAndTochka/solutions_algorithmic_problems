class Solution:
    def calculate_minimum_hp(self, dungeon: list[list[int]]) -> int:
        dungeon[-1][-1] = max(1 - dungeon[-1][-1], 1)

        for i in range(len(dungeon) - 2, -1, -1):
            dungeon[i][-1] = max(dungeon[i + 1][-1] - dungeon[i][-1], 1)

        for i in range(len(dungeon[0]) - 2, -1, -1):
            dungeon[-1][i] = max(dungeon[-1][i + 1] - dungeon[-1][i], 1)

        for i in range(len(dungeon) - 2, -1, -1):
            for j in range(len(dungeon[0]) - 2, -1, -1):
                dungeon[i][j] = max(
                    min(dungeon[i][j + 1], dungeon[i + 1][j]) - dungeon[i][j],
                    1
                )

        return dungeon[0][0]

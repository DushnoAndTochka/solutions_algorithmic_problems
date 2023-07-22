class Solution:
    def unique_paths_with_obstacles(
            self, obstacle_grid: list[list[int]]) -> int:
        if obstacle_grid[0][0] == 1:
            return 0

        result = [0] * len(obstacle_grid[0])
        for i in range(len(obstacle_grid[0])):
            if obstacle_grid[0][i] == 1:
                break
            result[i] = 1

        for i in range(1, len(obstacle_grid)):
            if result[0] and obstacle_grid[i][0]:
                result[0] = 0
            for j in range(1, len(obstacle_grid[i])):
                if obstacle_grid[i][j] == 1:
                    result[j] = 0
                else:
                    result[j] = result[j] + result[j - 1]

        return result[-1]

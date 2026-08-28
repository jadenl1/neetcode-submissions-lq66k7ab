class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0

        self.area = 0
        def dfs(i, j):
            if not (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0

                    self.area += 1

                    dfs(i+1, j) # down
                    dfs(i-1, j) # up
                    dfs(i, j+1) # right
                    dfs(i, j-1) # left

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.area = 0
                    dfs(i, j)
                    result = max(result, self.area)

        return result
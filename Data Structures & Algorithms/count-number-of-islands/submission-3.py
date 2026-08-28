class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        def dfs(i, j):
            if not (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    dfs(i+1, j) # down
                    dfs(i-1, j) # up
                    dfs(i, j+1) # right
                    dfs(i, j-1) # left
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    result += 1  
                    dfs(i, j)

        return result
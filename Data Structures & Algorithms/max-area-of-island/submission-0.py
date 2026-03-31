class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        seen = set()

        def findArea(grid, i, j):
            nonlocal seen
            nonlocal area
            if (i,j) not in seen and grid[i][j] == 1:
                area += 1
                seen.add((i,j))
                if i != 0: findArea(grid, i-1, j) # above
                if i != len(grid)-1: findArea(grid, i+1, j) # below
                if j != 0: findArea(grid, i, j-1) # left
                if j != len(grid[i])-1: findArea(grid, i, j+1) #right

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1 and (i,j) not in seen:
                    area = 0
                    findArea(grid, i, j)
                    maxArea = max(maxArea, area)
                    area = 0
        
        return maxArea

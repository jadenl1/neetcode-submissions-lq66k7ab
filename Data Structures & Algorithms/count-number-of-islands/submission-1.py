class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = [] # this will be a list of sets | list of tups | (col, row) of each seen 1
        seen = set()

        def createIsland(grid, i, j):
            nonlocal newIsland
            nonlocal seen
            if grid[i][j] == "1" and (i,j) not in newIsland:
                newIsland.add((i, j))
                seen.add((i,j))
                if i != 0: createIsland(grid, i-1, j) # above
                if i != len(grid)-1: createIsland(grid, i+1, j) # below
                if j != len(grid[i])-1: createIsland(grid, i, j+1) # right
                if j != 0: createIsland(grid, i, j-1) # left

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == "1" and (i, j) not in seen:
                    newIsland = set()
                    createIsland(grid, i, j)
                    islands.append(newIsland)
                    newIsland.clear()
        
        return len(islands)
from collections import defaultdict
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        taggedIslands = []
        for i in range(n):
            taggedIslands.append([0] * n)
        
        islandSizes = defaultdict(int)

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        tagId = 1
        for i in range(n):
            for j in range(n):
                if taggedIslands[i][j] == 0 and grid[i][j] == 1:
                    size = 0
                    stack = [(i, j)]
                    while stack:
                        r, c = stack.pop()
                        taggedIslands[r][c] = tagId
                        size += 1
                        for rChange, cChange in directions:
                            newR, newC = r + rChange, c + cChange
                            if newR in range(n) and newC in range(n) and taggedIslands[newR][newC] == 0 and grid[newR][newC] == 1:
                                taggedIslands[newR][newC] = tagId
                                stack.append((newR, newC))

                    islandSizes[tagId] = size
                    tagId += 1
        
        result = 0
        for tagId, islandSize in islandSizes.items():
            result = max(result, islandSize)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for iChange, jChange in directions:
                        newI, newJ = i + iChange, j + jChange
                        if newI in range(n) and newJ in range(n):
                            neighbors.add(taggedIslands[newI][newJ])
                    curr = 0
                    for neighbor in neighbors:
                        curr += islandSizes[neighbor]

                    result = max(result, curr + 1)
                        
        return result
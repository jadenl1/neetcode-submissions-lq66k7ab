class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, minSoFar, visited):
            result = [False, False]
            visited.add((r, c))
            minSoFar = min(minSoFar, heights[r][c])
            
            if r == 0 or c == 0:
                result[0] = True # Pacific
            if r == ROWS-1 or c == COLS-1:
                result[1] = True # Atlantic

            for rChange, cChange in directions:
                newR, newC = r + rChange, c + cChange
                if newR in range(ROWS) and newC in range(COLS) and heights[newR][newC] <= minSoFar and (newR, newC) not in visited:
                    pacific, atlantic = dfs(newR, newC, minSoFar, visited)
                    if pacific:
                        result[0] = True
                    if atlantic:
                        result[1] = True
            
            return result

        resultSet = set()
        for i in range(ROWS):
            for j in range(COLS):
                pacific, atlantic = dfs(i, j, heights[i][j], set())
                if pacific and atlantic:
                    resultSet.add((i, j))

        result = list()
        for i, j in resultSet:
            result.append([i,j])

        return result

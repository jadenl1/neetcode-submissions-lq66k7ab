class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, visited, maxSoFar):
            visited.add((r, c))
            maxSoFar = max(maxSoFar, heights[r][c])
            for rChange, cChange in directions:
                newR, newC = r + rChange, c + cChange
                if newR in range(ROWS) and newC in range(COLS) and (newR, newC) not in visited and heights[newR][newC] >= maxSoFar:
                    dfs(newR, newC, visited, maxSoFar)

        # pacific DFS
        pacific = set()

        i = 0
        for j in range(COLS):
            dfs(i, j, pacific, heights[i][j])
        
        j = 0
        for i in range(ROWS):
            dfs(i, j, pacific, heights[i][j])

        # atlantic DFS
        atlantic = set()
        i = ROWS-1
        for j in range(COLS):
            dfs(i, j, atlantic, heights[i][j])

        j = COLS-1
        for i in range(ROWS):
            dfs(i, j, atlantic, heights[i][j])

        result = []
        for tup in pacific:
            if tup in atlantic:
                result.append([tup[0], tup[1]])

        return result
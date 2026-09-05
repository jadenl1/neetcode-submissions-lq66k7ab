from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        q = deque()
        visited = set()
        fresh = 0
        result = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        # BFS
        while q:
            i, j, dist = q.popleft()

            validIndex = i >= 0 and i < ROWS and j >= 0 and j < COLS
            
            if validIndex and (i,j) not in visited and grid[i][j] != 0:
                
                if grid[i][j] == 1:
                    result = max(result, dist)
                    grid[i][j] = 2
                    fresh -= 1

                q.append((i-1, j, dist+1))
                q.append((i+1, j, dist+1))
                q.append((i, j-1, dist+1))
                q.append((i, j+1, dist+1))

            visited.add((i,j))
        
        if fresh > 0:
            return -1
        
        return result



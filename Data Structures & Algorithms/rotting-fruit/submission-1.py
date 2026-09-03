class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result = 0

        ROWS, COLS = len(grid), len(grid[0])
        
        q = deque() # (i, j)
        visited = set()

        fresh = 0
        
        # O(n^2)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j, 0))
        # O(n^2)
        while q:
            i, j, distance = q.popleft() # O(1)
            
            validIndex = (i >= 0 and i < ROWS and j >= 0 and j < COLS)
            
            if validIndex and (i,j) not in visited and grid[i][j] != 0:
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    fresh -= 1
                    
                result = max(result, distance)
                
                q.append((i-1,j, distance+1)) # up
                q.append((i+1,j, distance+1)) # down
                q.append((i,j-1, distance+1)) # left
                q.append((i,j+1, distance+1)) # right
                
                visited.add((i,j))
        
        if fresh > 0:
            return -1
        
        return result
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i+1,j,1))
                    q.append((i-1,j,1))
                    q.append((i,j+1,1))
                    q.append((i,j-1,1))
        
        while q:
            i, j, distance = q.popleft()
            validIndex = (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]))

            if validIndex and grid[i][j] != -1 and grid[i][j] != 0 and (i,j) not in visited:
                grid[i][j] = distance
            
                q.append((i+1,j,distance+1))
                q.append((i-1,j,distance+1))
                q.append((i,j+1,distance+1))
                q.append((i,j-1,distance+1))

            visited.add((i,j))
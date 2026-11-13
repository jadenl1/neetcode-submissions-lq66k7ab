from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        enclosed = []

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    visited = set()
                    q = deque([(i, j)])
                    safe = False
                    while q:
                        r, c = q.popleft()
                        visited.add((r, c))
                        if r == 0 or r == ROWS-1 or c == 0 or c == COLS-1:
                            safe = True
                        
                        for rChange, cChange in directions:
                            newR, newC = r + rChange, c + cChange
                            if newR in range(ROWS) and newC in range(COLS) and board[newR][newC] == 'O' and (newR, newC) not in visited:
                                visited.add((newR, newC))
                                q.append((newR, newC))
                    
                    if safe:
                        for r, c in visited:
                            board[r][c] = 'safe'
                    else:
                        for r, c in visited:
                            board[r][c] = 'X'

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'safe':
                    board[i][j] = 'O'

                        
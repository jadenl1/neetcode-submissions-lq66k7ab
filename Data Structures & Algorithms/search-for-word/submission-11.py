class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, count, visited):
            # print('visiting: ', r, c)
            visited.add((r, c))
            if count == len(word):
                return True
            for rChange, cChange in directions:
                newR = r + rChange
                newC = c + cChange
                if newR in range(0, ROWS) and newC in range(0, COLS) and (newR, newC) not in visited:
                    # print('neighbors: ', newR, newC)
                    if board[newR][newC] == word[count]:
                        if dfs(newR, newC, count + 1, set(visited)):
                            return True

            return False

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    print('new dfs..........@', i, j)
                    if dfs(i, j, 1, set()):
                        return True
        
        return False
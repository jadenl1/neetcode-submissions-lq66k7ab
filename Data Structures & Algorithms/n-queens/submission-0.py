class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = []
        for i in range(n):
            self.board.append(['.'] * n)
    
        self.result = list()

        self.usedCols = set()
        self.usedDownDiagonals = set()
        self.usedUpDiagonals = set()
        self.queens = 0
        def dfs(row):
            if row == n:
                if self.queens == n:
                    copy = []
                    for row in self.board:
                        copy.append(row.copy())
                    self.result.append(copy)
                return

            for col in range(len(self.board[row])):
                validPosition = col not in self.usedCols and (row - col) not in self.usedDownDiagonals and (row + col) not in self.usedUpDiagonals
                
                if validPosition:
                    self.board[row][col] = 'Q'
                    self.usedCols.add(col)
                    self.usedDownDiagonals.add(row - col)
                    self.usedUpDiagonals.add(row + col)
                    self.queens += 1

                    dfs(row + 1)

                    # backtrack
                    self.board[row][col] = '.'
                    self.usedCols.remove(col)
                    self.usedDownDiagonals.remove(row - col)
                    self.usedUpDiagonals.remove(row + col)
                    self.queens -= 1

        dfs(0)

        finalResult = []
        for board in self.result:
            finalBoard = []
            for row in board:
                finalBoard.append(''.join(row))
            finalResult.append(finalBoard)

        return finalResult
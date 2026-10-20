class Solution:
    def totalNQueens(self, n: int) -> int:
        self.result = 0

        usedCols = set()
        usedDowns = set() # row - col matches
        usedUps = set() # row + col matches
        def dfs(row):
            if row < n:
                for col in range(n):
                    available_position = col not in usedCols and row - col not in usedDowns and row + col not in usedUps
                    
                    if available_position:
                        usedCols.add(col)
                        usedDowns.add(row - col)
                        usedUps.add(row + col)

                        if row == n-1:
                            self.result += 1
                        
                        dfs(row + 1)

                        usedCols.remove(col)
                        usedDowns.remove(row - col)
                        usedUps.remove(row + col)

        dfs(0)

        return self.result
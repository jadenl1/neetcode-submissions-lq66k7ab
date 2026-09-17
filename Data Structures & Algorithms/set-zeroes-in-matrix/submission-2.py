class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        updateRows = set()
        updateCols = set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    updateRows.add(i)
                    updateCols.add(j)

        for row in updateRows:
            for j in range(COLS):
                matrix[row][j] = 0
            
        for col in updateCols:
            for i in range(ROWS):
                matrix[i][col] = 0

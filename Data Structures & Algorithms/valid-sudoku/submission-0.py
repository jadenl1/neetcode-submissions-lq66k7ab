class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check each row
        for row in board:
            seen = set()
            for item in row:
                if item != '.' and item in seen:
                    print("row fail")
                    return False
                seen.add(item)
        
        # check each col
        for i in range(9):
            seen = set()
            for j in range(9):
                item = board[j][i]
                if item != '.' and item in seen:
                    print("col fail")
                    return False
                seen.add(item)
        
        # check each 3x3 window
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                seen = set()
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if board[x][y] != '.' and board[x][y] in seen:
                            return False
                        seen.add(board[x][y])
                j += 3
            i += 3

        return True



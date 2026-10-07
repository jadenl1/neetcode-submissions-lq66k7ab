from collections import deque

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # construct a trie out of words
        class TrieNode:
            def __init__(self):
                self.isEndOfWord = False
                self.children = {}
                self.word = None
        
        root = TrieNode()

        def trieInsert(word):
            curr = root
            i = 0
            while i < len(word):
                char = word[i]
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                i += 1
            curr.isEndOfWord = True
            curr.word = word

        for word in words:
            trieInsert(word)

        # now traverse the board
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROWS, COLS = len(board), len(board[0])
        
        result = []

        def dfs(r, c, curr, visited):
            if curr.isEndOfWord:
                result.append(curr.word)
                curr.isEndOfWord = False

            visited.add((r, c))
            for rChange, cChange in directions:
                newR, newC = r + rChange, c + cChange
                if newR in range(ROWS) and newC in range(COLS) and board[newR][newC] in curr.children and (newR, newC) not in visited:
                    dfs(newR, newC, curr.children[board[newR][newC]], visited)
            
            visited.remove((r, c))

        for i in range(ROWS):
            for j in range(COLS):
                char = board[i][j]
                if char in root.children:
                    # begin the DFS
                    dfs(i, j, root.children[char], set())

        return result

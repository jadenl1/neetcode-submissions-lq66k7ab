class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.parenthesis = ''

        self.left = 0
        self.right = 0

        def dfs():
            print(self.parenthesis)
            if self.left == n and self.right == n:
                result.append(self.parenthesis)
                return

            if self.left < n:
                self.parenthesis += '('
                self.left += 1
                dfs()
                self.parenthesis = self.parenthesis[:-1]
                self.left -= 1
            
            if self.right < self.left:
                self.parenthesis += ')'
                self.right += 1
                dfs()
                self.parenthesis = self.parenthesis[:-1]
                self.right -= 1

        dfs()
        return result

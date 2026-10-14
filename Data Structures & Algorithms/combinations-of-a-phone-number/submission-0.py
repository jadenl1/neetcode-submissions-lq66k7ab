class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'prqs', '8':'tuv', '9':'wxyz'}
        
        result = []
        state = []

        def dfs(i):
            if i < len(digits):
                for char in phone[digits[i]]:
                    state.append(char)
                    dfs(i+1)
                    state.pop()
            else:
                if state:
                    result.append(''.join(state))
        
        dfs(0)

        return result
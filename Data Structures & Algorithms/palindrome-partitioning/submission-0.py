class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []

        state = []
        def dfs(i):
            if i >= n:
                result.append(state.copy())
            else:
                for x in range(i, n):
                    substr = s[i:x+1]
                    # print(substr)
                    if substr == substr[::-1]:
                        state.append(substr)
                        dfs(x+1)
                        state.pop()
        
        dfs(0)

        return result

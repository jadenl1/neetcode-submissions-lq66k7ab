class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        state = []
        def dfs(x):
            result.append(state.copy())
            for i in range(x, n):
                state.append(nums[i])
                dfs(i+1)
                state.pop()
        
        dfs(0)

        return result
                
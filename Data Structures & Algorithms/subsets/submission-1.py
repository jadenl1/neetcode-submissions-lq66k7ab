class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        state = []
        def dfs(i):
            if i < len(nums):
                for x in range(i, len(nums)):
                    num = nums[x]
                    state.append(num)
                    result.append(state.copy())
                    dfs(x+1)
                    state.pop()

        dfs(0)
                
        return result
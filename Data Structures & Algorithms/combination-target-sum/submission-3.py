class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        state = []
        def dfs(i, currentSum):
            if currentSum >= target:
                if currentSum == target:
                    result.append(state.copy())
                return

            for x in range(i, len(nums)):
                num = nums[x]
                state.append(num)
                dfs(x, currentSum + num)
                state.pop()
                
        dfs(0, 0)

        return result
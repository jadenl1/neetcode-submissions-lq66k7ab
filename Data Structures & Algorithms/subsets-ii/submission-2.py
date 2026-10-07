class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]

        state = []
        def dfs(i):
            if i < len(nums):
                for x in range(i, len(nums)):
                    num = nums[x]
                    if x != i and num == nums[x-1]:
                        continue

                    state.append(num)
                    result.append(state.copy())
                    dfs(x + 1)
                    state.pop()
        
        dfs(0)

        return result

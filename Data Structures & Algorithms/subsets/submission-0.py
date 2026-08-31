class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(index):
            if index >= len(nums):
                result.append(subset.copy())
                return
            
            # choices
            # include the current index
            subset.append(nums[index])
            dfs(index + 1)

            # dont include the current index
            subset.pop() # remove the element
            dfs(index + 1)

        dfs(0)
        return result
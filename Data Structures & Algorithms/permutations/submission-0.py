class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []

        def dfs():
            if len(permutation) == len(nums):
                result.append(permutation.copy())
                return
            
            currentPermutation = set(permutation)
            for choice in nums:
                if choice not in currentPermutation:
                    permutation.append(choice)
                    dfs()
                    permutation.pop()
        
        dfs()
        return result
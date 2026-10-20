class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        result = 0
        
        for num in nums:
            if num - 1 not in numset:
                curr = 1
                while num + curr in numset:
                    curr += 1
                result = max(result, curr)
        
        return result
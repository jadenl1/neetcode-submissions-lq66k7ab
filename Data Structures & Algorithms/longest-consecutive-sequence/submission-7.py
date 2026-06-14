class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        result = 0
        numset = set(nums)

        for num in nums:
            # start of a seq
            if num - 1 not in numset:
                k = 1
                while num + k in numset:
                    k += 1
                result = max(result, k)
            
        return result

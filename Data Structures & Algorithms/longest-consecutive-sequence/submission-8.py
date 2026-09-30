class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        numset = set(nums)

        for i, num in enumerate(nums):
            if num - 1 not in numset:
                count = 1
                while num + count in numset:
                    count += 1
                result = max(result, count)
        
        return result
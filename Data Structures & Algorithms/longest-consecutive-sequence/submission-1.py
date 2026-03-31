class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        maxLength = 0

        for num in numSet:
            if num-1 not in numSet:
                length = 0
                curr = num
                while curr in numSet:
                    curr += 1
                    length += 1
                if length > maxLength:
                    maxLength = length
        
        return maxLength
                
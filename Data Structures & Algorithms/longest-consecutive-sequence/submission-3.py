class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxLength = 0
        for num in numSet:
            if num - 1 not in numSet:
                # then we start going forward
                length = 1
                while num + length in numSet:
                    length += 1
                if length > maxLength:
                    maxLength = length
        return maxLength
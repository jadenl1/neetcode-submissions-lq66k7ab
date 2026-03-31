class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        result = 0

        for num in nums:
            # we are at the beginning of a potential consectutive sequence
            if num-1 not in numset:
                count = 1
                # go forward as far as possible
                while num+count in numset:
                    count += 1

                result = max(result, count)
        
        return result
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        numset = set(nums)
        longest = 1

        for num in nums:
            count = 0
            if num-1 not in numset:
                #start of a sequence, keep going until seq stops
                while num+count in numset:
                    count+=1
                if count > longest:
                    longest = count
            
        return longest
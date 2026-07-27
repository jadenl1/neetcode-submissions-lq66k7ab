class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [1,2,3,2,2]       n=4 -> 1,2,3,4

        
        for i, num in enumerate(nums):
            curr = abs(num)
            if nums[curr] < 0:
                return curr
            else:
                nums[curr] = nums[curr] * -1
            
        
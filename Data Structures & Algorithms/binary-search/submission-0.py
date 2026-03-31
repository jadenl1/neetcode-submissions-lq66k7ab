class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high: # ?

            midi = low + ((high-low)//2)
            mid = nums[midi]
            
            if mid == target:
                return midi
            elif mid < target:
                low = midi + 1
            elif mid > target:
                high = midi - 1

        return -1

        #mid -> (n-1)/2
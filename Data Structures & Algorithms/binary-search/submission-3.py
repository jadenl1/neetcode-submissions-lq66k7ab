class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            midi = lo + ((hi - lo) // 2)
            mid = nums[midi]
            if mid == target:
                return midi
            elif mid < target:
                lo = midi + 1
            else:
                hi = midi - 1
        
        return -1
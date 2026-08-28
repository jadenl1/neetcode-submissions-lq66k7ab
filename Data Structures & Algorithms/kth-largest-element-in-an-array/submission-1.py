import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = 0

        for i, num in enumerate(nums):
            nums[i] = -num
        
        heapq.heapify(nums)

        while k > 0:
            result = heapq.heappop(nums)
            k -= 1

        return -result
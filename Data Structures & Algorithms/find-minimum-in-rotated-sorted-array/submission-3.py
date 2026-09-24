class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        result = float('inf')

        while l <= r:
            m = (l + r) // 2

            left = nums[l]
            right = nums[r]
            mid = nums[m]

            if left <= mid <= right:
                return min(left, result)
            elif mid <= right and mid <= left:
                result = min(result, mid)
                r = m - 1
            elif mid >= right and mid >= left:
                l = m + 1

        return result
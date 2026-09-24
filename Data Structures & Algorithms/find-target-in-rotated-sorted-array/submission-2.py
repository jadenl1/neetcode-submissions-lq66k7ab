class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l + r) // 2

            left, right, mid = nums[l], nums[r], nums[m]

            if mid == target:
                return m

            if mid <= right <= left:
                if mid <= target <= right:
                    l = m + 1
                else:
                    r = m - 1
            elif right <= left <= mid:
                if left <= target <= mid:
                    r = m - 1
                else:
                    l = m + 1
            elif left <= mid <= right:
                if target < mid:
                    r = m - 1
                else:
                    l = m + 1
                    
        return -1
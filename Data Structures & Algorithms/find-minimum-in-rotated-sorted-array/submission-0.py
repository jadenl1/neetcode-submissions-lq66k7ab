class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        l = 0
        r = n-1

        mMin = float('inf')

        while l <= r:
            m = (l + r) // 2
            
            rVal, lVal, mVal = nums[r], nums[l], nums[m]

            mMin = min(mMin, mVal)

            if rVal < lVal <= mVal:
                l = m + 1
            elif mVal <= rVal < lVal:
                r = m - 1
            else:
                r = m - 1

        
        return mMin
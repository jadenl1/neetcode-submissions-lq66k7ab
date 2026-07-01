class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l = 0
        r = n-1

        while l <= r:
            m = (l + r) // 2

            lVal, mVal, rVal = nums[l], nums[m], nums[r]

            if mVal == target:
                return m

            # is m in left or right part of list
            if lVal <= mVal:
                # m is in left side of the list
                if mVal < target:
                    l = m + 1 # always search right
                else: # mVal > target
                    if target < lVal:
                        l = m + 1
                    else:
                        r = m - 1
            else:
                # m is in right side
                if mVal > target:
                    r = m - 1
                else:
                    if target > rVal:
                        r = m - 1
                    else:
                        l = m + 1
            
        return -1
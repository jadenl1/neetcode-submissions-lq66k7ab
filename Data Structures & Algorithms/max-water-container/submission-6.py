class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1

        result = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            result = max(result, area)

            if heights[l] <= heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
        
        return result
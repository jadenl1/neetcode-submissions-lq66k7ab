class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        result = 0
        l = 0
        r = n-1

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            result = max(result, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return result
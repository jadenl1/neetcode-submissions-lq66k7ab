class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            currWater = min(heights[l], heights[r]) * (r - l)
            maxWater = max(currWater, maxWater)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater
        

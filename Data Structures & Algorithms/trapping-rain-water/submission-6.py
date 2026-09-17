class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n

        leftMax, rightMax = 0, 0
        for i in range(n):
            leftHeight, rightHeight = height[i], height[n-i-1]
            if leftHeight > leftMax:
                leftMax = leftHeight
            if rightHeight > rightMax:
                rightMax = rightHeight
            left[i] = leftMax
            right[n-i-1] = rightMax
            
        result = 0
        for i, currHeight in enumerate(height):
            minimum = min(left[i], right[i])
            if minimum > currHeight:
                result += (minimum - height[i])
        
        return result
            

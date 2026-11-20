class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        n = len(height)

        left = [0] * n
        right = [0] * n

        runningMaxLeft = 0
        runningMaxRight = 0
        for i in range(n):
            left[i] = runningMaxLeft
            right[n-i-1] = runningMaxRight
            runningMaxLeft = max(runningMaxLeft, height[i])
            runningMaxRight = max(runningMaxRight, height[n-i-1])
        
        for i in range(n):
            currMin = min(left[i], right[i])
            if height[i] < currMin:
                result += (currMin - height[i])

        return result
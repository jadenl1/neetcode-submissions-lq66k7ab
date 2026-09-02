class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # for each position the tallest height on the left of height[i] -> leftMax[i]
        leftMax = [0] * n
        # the tallest height on the right of height[i] -> rightMax[i]
        rightMax = [0] * n

        # populate both
        leftMaxSoFar = height[0]
        rightMaxSoFar = height[n-1]
        for i in range(n):
            leftMax[i] = leftMaxSoFar
            leftMaxSoFar = max(leftMaxSoFar, height[i])
            rightMax[n-i-1] = rightMaxSoFar
            rightMaxSoFar = max(rightMaxSoFar, height[n-i-1])

        result = 0
        
        i = 0
        while i < n:
            # at each spot, we can hold the min(left, right) IFF its greater than the current height
            if height[i] <= min(leftMax[i], rightMax[i]):
                result += min(leftMax[i], rightMax[i]) - height[i]
            i += 1

        return result


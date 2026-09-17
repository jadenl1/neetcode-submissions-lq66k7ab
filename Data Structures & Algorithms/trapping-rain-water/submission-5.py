class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n

        # prefix
        maxHeight = 0
        for i, currHeight in enumerate(height):
            if currHeight > maxHeight:
                maxHeight = currHeight
            left[i] = maxHeight
        
        # postfix
        maxHeight = 0
        for i, currHeight in enumerate(reversed(height)):
            if currHeight > maxHeight:
                maxHeight = currHeight
            right[n-i-1] = maxHeight
        
        result = 0
        for i, currHeight in enumerate(height):
            # print(i, 'height:', currHeight, '| left, right:', left[i], right[i])
            minimum = min(left[i], right[i])
            if minimum > currHeight:
                # print('water! ', minimum)
                result += (minimum - height[i])
        
        return result
            

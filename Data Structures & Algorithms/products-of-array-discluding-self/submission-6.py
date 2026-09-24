class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [nums[0]] * n
        right = [nums[-1]] * n

        for i in range(1, n):
            left[i] = left[i-1] * nums[i]
            right[n-i-1] = right[n-i] * nums[n-i-1]
        
        result = [0] * n
        for i in range(n):
            if i == 0:
                result[i] = right[1]
            elif i == n-1:
                result[i] = left[n-2]
            else:
                result[i] = left[i-1] * right[i+1]

        return result
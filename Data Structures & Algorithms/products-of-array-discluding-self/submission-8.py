class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        post = [0] * n

        for i in range(n):
            if i == 0:
                pre[i] = nums[i]
                post[n-i-1] = nums[n-i-1]
            else:
                pre[i] = pre[i-1] * nums[i]
                post[n-i-1] = post[n-i] * nums[n-i-1]
        
        result = [0] * n
        for i in range(n):
            if i == 0:
                result[i] = post[i+1]
            elif i == n-1:
                result[i] = pre[i-1]
            else:
                result[i] = pre[i-1] * post[i+1]

        return result
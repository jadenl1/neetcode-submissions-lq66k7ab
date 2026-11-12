class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        post = [0] * n

        pre[0] = nums[0]
        post[n-1] = nums[n-1]
        for i in range(1, n-1):
            pre[i] = pre[i-1] * nums[i]
            post[n-i-1] = post[n-i] * nums[n-i-1]
        
        result = [0] * n
        result[0] = post[1]
        result[n-1] = pre[n-2]

        for i in range(1, n-1):
            result[i] = pre[i-1] * post[i+1]

        return result
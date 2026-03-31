class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []

        n = len(nums)

        # build pre and postfix arrs, where its a compounding product going both ways
        for i in range(n):
            if i == 0:
                pre.append(nums[i])
                post.append(nums[n-i-1])
            else:
                pre.append(nums[i] * pre[i-1])
                post.append(nums[n-i-1] * post[i-1])
        
        post.reverse()
        print(pre)
        print(post)

        result = []
        for i in range(n):
            if i == 0:
                result.append(post[i+1])
            elif i == n-1:
                result.append(pre[i-1])
            else:
                result.append(pre[i-1] * post[i+1])

        return result

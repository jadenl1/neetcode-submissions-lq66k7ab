class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1 2 4 6]

        # pre: [1 2 8 48]
        # post: [48 48 24 6]



        # for current value @ index i
        # we do pre[i-1] * post[i+1]

        n = len(nums)

        pre = [1] * n
        post = [1] * n

        for i in range(n):
            if i == 0:
                pre[i] = nums[i]
                post[i] = nums[n-1]
            else:
                pre[i] = pre[i-1] * nums[i]
                post[i] = post[i-1] * nums[n-i-1]

        post.reverse()

        print(pre)
        print(post)

        result = [1] * n

        for i in range(n):
            if i == 0:
                result[i] = post[i+1]
            elif i == n-1:
                result[i] = pre[i-1]
            else:
                result[i] = pre[i-1] * post[i+1]
        
        return result

        
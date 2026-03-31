class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productsForward = []
        productsBackward = []

        currproduct = 1
        for i, num in enumerate(nums):
            currproduct *= num
            productsForward.append(currproduct)

        currproduct = 1
        for i in range(len(nums)-1, -1, -1):
            currproduct *= nums[i]
            productsBackward.insert(0, currproduct)
        
        print(productsForward)
        print(productsBackward)

        res = []

        for i in range(len(productsForward)):
            if i == 0:
                res.append(productsBackward[i+1])
            elif i == len(productsForward)-1:
                res.append(productsForward[i-1])
            else:
                res.append(productsForward[i-1] * productsBackward[i+1])

        return res
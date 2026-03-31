class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first thing i think is O(n^2), lets code that
        # loop through nums

        res = []

        for i in range(len(nums)):
            #loop again through nums

            product = 1

            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
                    print(product)
        
            res.append(product)

        return res
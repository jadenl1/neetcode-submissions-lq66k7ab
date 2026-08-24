class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        n = len(nums)
        nums.sort()

        for i in range(n):
            l = i+1
            r = n-1

            while l < r and r >= 0 and l < n and (nums[l] <= 0 or nums[r] >= 0):
                triple = nums[l] + nums[i] + nums[r]

                if triple < 0:
                    l += 1
                elif triple > 0:
                    r -= 1
                else: # hit
                    tup = [nums[l], nums[i], nums[r]]
                    tup.sort()
                    result.add(tuple(tup))
                    l += 1
                    r -= 1

        output = []
        for tup in result:
            output.append(list(tup))

        return output
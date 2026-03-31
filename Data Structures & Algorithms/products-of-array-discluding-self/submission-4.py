class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        forward = []
        backward = []
        revNums = nums[::-1]
        for i in range(len(nums)):
            if i == 0:
                forward.append(nums[i])
                backward.append(revNums[i])
            else:
                forward.append(forward[i-1] * nums[i])
                backward.append(backward[i-1] * revNums[i])

        print(forward)
        backward.reverse()
        print(backward)

        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(backward[i+1])
            elif i == len(nums)-1:
                result.append(forward[i-1])
            else:
                result.append(forward[i-1] * backward[i+1])

        return result
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                return num
            nums[num - 1] *= -1
            print(nums)
        
        return -1

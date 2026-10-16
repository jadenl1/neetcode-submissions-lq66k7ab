class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = dict()

        for i, num in enumerate(nums):
            if target - num in diffs:
                return [diffs[target - num], i]
            diffs[num] = i
        
        return [-1, -1]
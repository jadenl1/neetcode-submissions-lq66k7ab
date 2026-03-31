class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {} # target: index

        for i, num in enumerate(nums):
            inverse = target - num

            if num in maps:
                return [maps[num], i]
            
            maps[inverse] = i

        return []




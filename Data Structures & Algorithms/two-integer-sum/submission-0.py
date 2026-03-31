class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # counter : value
        # {4:0, } if we have map[curr] then return [nums[map[curr]], map[curr]]

        dictionary = {}

        for i, num in enumerate(nums):

            inv = target - num

            if dictionary.get(num) != None:
                return [dictionary[num], i]
            else:
                dictionary[inv] = i

        return []

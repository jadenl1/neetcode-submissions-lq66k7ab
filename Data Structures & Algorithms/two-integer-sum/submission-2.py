class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {} # {compliment:index}

        for i, num in enumerate(nums):
            if num in mydict:
                return [mydict[num], i]
            
            compliment = target - num
            mydict[compliment] = i
        
        return [-1, -1]
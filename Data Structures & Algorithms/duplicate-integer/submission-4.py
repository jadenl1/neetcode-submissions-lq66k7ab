from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsCount = Counter(nums)
        for key, value in numsCount.items():
            if value > 1:
                return True
    
        return False
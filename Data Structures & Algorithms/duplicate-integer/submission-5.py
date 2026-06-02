class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        
        for num in nums:
            counts[num] += 1
        
        for num, count in counts.items():
            if count > 1:
                return True

        return False
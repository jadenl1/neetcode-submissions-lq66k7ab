class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        l = 0
        r = n - 1

        total = numbers[l] + numbers[r]
        while total != target:
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            total = numbers[l] + numbers[r]
        
        return [l+1, r+1]
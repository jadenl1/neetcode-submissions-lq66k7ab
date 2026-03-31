class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        rlsum = numbers[l] + numbers[r]
        while rlsum != target:
            if rlsum < target:
                l += 1
            elif rlsum > target:
                r -= 1
            rlsum = numbers[l] + numbers[r]
        
        return [l+1, r+1]
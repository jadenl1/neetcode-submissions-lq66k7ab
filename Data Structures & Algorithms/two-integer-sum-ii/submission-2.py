class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while numbers[l] + numbers[r] != target:
            psum = numbers[l] + numbers[r]
            if psum < target:
                l += 1
            elif psum > target:
                r -= 1
            
        return [l+1,r+1]
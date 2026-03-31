class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pl = 0
        pr = len(numbers)-1

        res = 0

        while pl < pr:
            left = numbers[pl]
            right = numbers[pr]

            res = left + right

            if res < target:
                pl += 1
            elif res > target:
                pr -= 1
            elif res == target:
                break
        
        return [pl+1, pr+1]
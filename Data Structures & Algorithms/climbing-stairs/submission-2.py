class Solution:
    def climbStairs(self, n: int) -> int:
        # steps arr, at steps[n] we know that it will be
        # steps[n-1] + 1 is one way
        # steps[n-2] + 3 (we can do s[n-2] + 1 + 1 or s[n-2] + 2) is another
        if n <= 2: return n

        steps = [0] * (n + 1)
        steps[1] = 1
        steps[2] = 2

        for i in range(3, n + 1):
            steps[i]+= steps[i-1] + steps[i-2]
        
        print(steps)

        return steps[n]
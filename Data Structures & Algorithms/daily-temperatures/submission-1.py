class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [(temp, index), ..]
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            
            # while current temperature > top of stack
            while stack and temp > stack[-1][0]:
                # pop the stack?
                print(stack)
                t, index = stack.pop()
                res[index] = i - index
                
            stack.append((temp, i))
            
        return res # ?





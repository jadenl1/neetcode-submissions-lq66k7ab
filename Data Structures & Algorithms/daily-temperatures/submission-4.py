class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                popped = stack.pop()
                result[popped[1]] = i - popped[1]
            stack.append(tuple([temp, i]))
        
        return result
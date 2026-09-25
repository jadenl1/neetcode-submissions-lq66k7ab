class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # (temp, index)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                result[stackIdx] = i - stackIdx
            
            stack.append((temp, i))

        return result
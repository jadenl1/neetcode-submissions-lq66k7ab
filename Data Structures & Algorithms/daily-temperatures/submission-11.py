class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = [(0, temperatures[0])]

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                past_index = stack.pop()[0]
                result[past_index] = i - past_index
            stack.append((i, temp))
        
        return result
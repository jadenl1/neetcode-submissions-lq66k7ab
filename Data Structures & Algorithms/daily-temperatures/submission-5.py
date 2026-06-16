class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # using stack
        n = len(temperatures)
        result = [0] * n

        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                popIdx = stack.pop()[1]
                result[popIdx] = i - popIdx
            
            stack.append((temp, i))

        return result
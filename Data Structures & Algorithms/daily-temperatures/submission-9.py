class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []

        result = [0] * n

        for i, temp in enumerate(temperatures):
            curr = (i, temp) # tup[0] -> index, tup[1] -> temp
            if not stack:
                stack.append(curr)
                continue
                        
            top = stack[-1] # peek

            while stack and top[1] < curr[1]:

                stack.pop()
                result[top[0]] = curr[0] - top[0]
                if stack:
                    top = stack[-1]
            
            stack.append(curr)
            
        
        return result
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack : [(30, 0)] (38, 1)
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            print('current:', i)
            print(temp)
            print('stack:', stack)
            print(result)
            print('.........')
            if not stack:
                stack.append((i, temp))
                continue
            
            while stack and stack[-1][1] < temp:
                popped = stack.pop()
                result[popped[0]] = i - popped[0]
            
            stack.append((i, temp))

        return result
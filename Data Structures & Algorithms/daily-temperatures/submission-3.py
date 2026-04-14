class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        # 30 

        for i, temp in enumerate(temperatures):
            print('curr: ', i)
            while stack and temp > stack[-1][0]:
                popped = stack.pop()
                print('popped! ', popped)
                result[popped[1]] = i - popped[1]

            stack.append(tuple([temp, i]))
            print(stack)
        
        return result
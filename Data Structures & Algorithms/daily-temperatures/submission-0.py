class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #coding the O(n^2) solution
        res = []
        
        # loop through each temp
        for i, temp in enumerate(temperatures):
            # loop past temp until greater num than temp
            count = 0
            for j in range(i, len(temperatures), 1):
                if j == len(temperatures) - 1 and temperatures[j] <= temp:
                    count = 0
                    break
                    
                # temperatures[j] is going forward from i now
                if temperatures[j] > temp:
                    break
                count += 1

            res.append(count)
        return res
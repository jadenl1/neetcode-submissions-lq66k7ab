class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        result = [0] * len(temps)
        i = 0
        while i < len(temps):
            days = 0
            j = i
            while j < len(temps)-1 and temps[j] <= temps[i]:
                j += 1
            if temps[j] > temps[i]:
                days = j - i
                result[i] = days
            else:
                result[i] = 0
            i += 1

        return result
        
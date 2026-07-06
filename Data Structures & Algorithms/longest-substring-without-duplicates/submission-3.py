class Solution:
    def printSet(self, s):
        for value in s:
            print(value, end=' ')
        print(' ')

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n == 0 or n == 1:
            return n

        strset = set()
        strset.add(s[0])
        result = 1

        l = 0
        r = 1

        while r < n:
            self.printSet(strset)
            if s[r] not in strset:
                strset.add(s[r])
                r += 1
            else:
                strset.remove(s[l])
                result = max(result, r - l)
                l += 1

        return max(result, r - l)
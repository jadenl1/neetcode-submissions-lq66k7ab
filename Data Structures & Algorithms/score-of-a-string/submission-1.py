class Solution:
    def scoreOfString(self, s: str) -> int:
        if len(s) == 2:
            return abs(ord(s[0]) - ord(s[1]))
        
        res = 0
        for i in range(len(s)-1):
            res += abs(ord(s[i]) - ord(s[i+1]))
        return res
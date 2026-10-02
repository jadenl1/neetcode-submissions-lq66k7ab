class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        
        sPtr = 0
        tPtr = 0

        while tPtr < len(t):
            if sPtr < len(s) and s[sPtr] == t[tPtr]:
                sPtr += 1
            tPtr += 1

        return sPtr == len(s)
        
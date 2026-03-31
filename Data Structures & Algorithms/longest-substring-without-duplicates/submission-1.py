class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        l = 0
        r = 1

        res = 0

        while l <= r and r <= len(s)-1:
            print(s[l:r])
            if s[r] not in s[l:r]:
                r += 1
            else:
                l += 1
            
            res = max(res, r-l)

        return res
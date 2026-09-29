class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = [0, 0]

        for i in range(n):
            l, r = i, i
            while (l - 1) >= 0 and (r + 1) < n and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            if (r - l + 1) > (result[1] - result[0] + 1):
                result[0] = l
                result[1] = r
            
            l, r = i, i + 1
            if l in range(n) and r in range(n) and s[l] == s[r]:
                while (l - 1) >= 0 and (r + 1) < n and s[l - 1] == s[r + 1]:
                    l -= 1
                    r += 1
                if (r - l + 1) > (result[1] - result[0] + 1):
                    result[0] = l
                    result[1] = r
        
        return s[result[0]:result[1]+1]
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        result = [0, 0]
        for i in range(n):            
            # odd case <-a->
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
        
            if (r - l - 1) > (result[1] - result[0] - 1):
                result[0], result[1] = l, r

            # even case <-aa->
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
        
            if (r - l - 1) > (result[1] - result[0] - 1):
                result[0], result[1] = l, r
        
        return s[result[0]+1:result[1]]
        
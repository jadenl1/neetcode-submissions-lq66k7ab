class Solution:
    def isPalindrome(self, s: str) -> bool:
        pf = 0
        pb = len(s) - 1

        # .isalnum() 
        # remove all non-alnum chars in s
        newStr = ""
        for char in s.replace(" ", ""):
            if char.isalnum():
                newStr += char.lower()
        
        return newStr == newStr[::-1]

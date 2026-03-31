class Solution:
    def isPalindrome(self, s: str) -> bool:

        # remove all non-alnum chars in s
        newStr = ""
        for char in s.replace(" ", ""):
            if char.isalnum():
                newStr += char.lower()
        
        # return newStr == newStr[::-1], works too easy

        # two-pointer
        pf = 0
        pb = len(newStr) - 1

        while pf < pb:
            if newStr[pf] != newStr[pb]:
                return False
            pf += 1
            pb -= 1

        return True
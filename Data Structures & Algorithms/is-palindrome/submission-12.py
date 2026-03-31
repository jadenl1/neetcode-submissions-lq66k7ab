class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean string
        string = ''
        for ch in s:
            if ch.isalnum():
                string += ch.lower()

        return string == string[::-1]
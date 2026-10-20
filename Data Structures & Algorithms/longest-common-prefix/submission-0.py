class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        smallestWord = min(strs)

        i = 0
        while i < len(smallestWord):
            char = smallestWord[i]
            trav = True
            for word in strs:
                if word[i] != char:
                    trav = False

            if not trav:
                break
            i += 1
      
        return smallestWord[0:i]
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord('a')] += 1

            tup = tuple(counts)
            mydict[tup].append(s)
        
        result = []
        for key, value in mydict.items():
            result.append(value)

        return result
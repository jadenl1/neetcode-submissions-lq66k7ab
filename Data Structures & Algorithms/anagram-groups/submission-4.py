class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        
        for string in strs:
            letters = [0] * 26
            for char in string:
                letters[ord(char) - ord('a')] += 1
            
            tup = tuple(letters)
            mydict[tup].append(string)

        result = []
        for key, value in mydict.items():
            result.append(value)

        return result
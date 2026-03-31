class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)

        for string in strs:
            key = [0] * 26
            counts = Counter(string)

            for letter, count in counts.items():
                key[ord(letter) - ord('a')] += count
            
            mydict[tuple(key)].append(string)
        
        return(list(mydict.values()))

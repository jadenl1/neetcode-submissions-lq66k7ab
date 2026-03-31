class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)

        for string in strs:
            tup = [0] * 26
            
            for char in string:
                tup[ord('a') - ord(char)] += 1
            
            maps[tuple(tup)].append(string)
            
        return maps.values()
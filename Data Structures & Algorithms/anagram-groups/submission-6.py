class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for string in strs:
            counts = [0] * 26 # store the count of each letter
            for char in string:
                counts[ord(char) - ord('a')] += 1
            
            tup = tuple(counts)
            groups[tup].append(string)

        result = []
        for value in groups.values():
            result.append(list(value))

        return result

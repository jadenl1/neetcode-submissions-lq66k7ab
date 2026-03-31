class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for string in strs:
            counts = [0] * 26 # store the count of each letter
            countMap = Counter(string)
            for letter, count in countMap.items():
                counts[ord(letter) - ord('a')] += count
            
            tup = tuple(counts)
            groups[tup].append(string)

        result = []
        for value in groups.values():
            result.append(list(value))

        return result

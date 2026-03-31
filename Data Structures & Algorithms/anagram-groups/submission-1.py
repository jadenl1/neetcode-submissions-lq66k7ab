class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            # make an array for the counts of each letter (26 spaces for each)
            counts = [0] * 26
            for char in string:
                counts[ord(char) - ord('a')] += 1
            
            result[tuple(counts)].append(string)

        return list(result.values())


 
                    

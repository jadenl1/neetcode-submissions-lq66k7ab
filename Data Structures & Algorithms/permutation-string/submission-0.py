from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = Counter(s1)

        for i in range(len(s2) - len(s1) + 1):
            substr = s2[i:i+len(s1)]
            substr_counts = Counter(substr)

            if substr_counts == counts:
                return True
        
        return False


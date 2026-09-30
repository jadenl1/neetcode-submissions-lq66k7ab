from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_counts = Counter(s1)

        for i, ch in enumerate(s2):
            if ch in s1_counts:
                counts_copy = dict(s1_counts)
                curr = 0
                while i + curr in range(len(s2)) and s2[i + curr] in counts_copy:
                    counts_copy[s2[i + curr]] -= 1
                    if counts_copy[s2[i + curr]] <= 0:
                        del counts_copy[s2[i + curr]]
                    curr += 1
                if curr == len(s1):
                    return True
        
        return False

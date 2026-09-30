from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_counts = Counter(s1)

        l = 0
        r = 0
        window = defaultdict(int)
        while r < len(s1):
            window[s2[r]] += 1
            r += 1

        r -= 1

        while r < len(s2):
            if window == s1_counts:
                return True

            r += 1
            if r < len(s2):
                window[s2[r]] += 1
            if l < len(s2):
                window[s2[l]] -= 1
                if window[s2[l]] <= 0:
                    del window[s2[l]]
            l += 1

        return False

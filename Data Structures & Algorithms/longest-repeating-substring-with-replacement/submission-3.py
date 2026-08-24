class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        result = 0

        windowCounts = defaultdict(int)

        l = 0
        r = 0

        windowCounts[s[0]] += 1

        while r < n:
            # print('l: ', l, 'r: ', r)
            # print('counts: ', windowCounts)
            # print('...........')
            # find most freq. element
            maxFreq = 0
            for key, value in windowCounts.items():
                maxFreq = max(maxFreq, value)
            
            if (r - l + 1) - maxFreq <= k:
                # print('^^ valid window of length ', r-l+1)
                result = max(result, r - l + 1)
                r += 1
                if r < n:
                    windowCounts[s[r]] += 1
            else:
                windowCounts[s[l]] -= 1
                l += 1

        return result
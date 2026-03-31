class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #[][][] index->count of elem
        counts = Counter(nums) # {num: count, num: count, ...}

        maxCount = max(counts.values())
        

        buckets = []
        for i in range(maxCount):
            buckets.append([])

        for num, count in counts.items():
            buckets[count-1].append(num)

        result = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) >= k:
                    return result
        
        return result
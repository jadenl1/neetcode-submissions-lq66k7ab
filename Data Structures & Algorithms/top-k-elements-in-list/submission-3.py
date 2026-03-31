class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
    
        for i in range(len(nums)):
            buckets.append([])

        counts = Counter(nums)

        for num, count in counts.items():
            buckets[count-1].append(num)
        
        print(buckets)
        
        res = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        for n in nums:
            buckets.append(list())
        
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1

        for num, count in counts.items():
            buckets[count-1].append(num)

        result = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                if len(result) == k:
                    return result
                result.append(num)


        return result
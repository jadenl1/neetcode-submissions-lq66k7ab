from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count all elems in dictionary
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        # make buckets
        maxCount = max(counts.values())
        
        buckets = []
        for i in range(maxCount):
            buckets.append([])

        # populate buckets
        for num, count in counts.items():
            buckets[count-1].append(num)

        result = []
        for bucket in reversed(buckets):
            for item in bucket:
                if len(result) >= k:
                    return result
                result.append(item)
        
        return result
            


import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        #count nums
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        #count ex. {7: 2}

        # now we use buckets
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        
        for num, count in counts.items():
            buckets[count].append(num)
        
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result


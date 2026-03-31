import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        #count nums
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        #count ex. {7: 2}

        # now we use a heap
        heap = []
        for num, freq in count.items():
            heap.append( (-freq, num) )
        heapq.heapify(heap)

        result = []
        for i in range(k):
            popped = heapq.heappop(heap)[1]
            result.append(popped)
        
        return result

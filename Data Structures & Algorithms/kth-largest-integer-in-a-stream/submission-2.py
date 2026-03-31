import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # min heap
        self.minHeap = nums
        self.k = k
        # we heapify what we have so far
        heapq.heapify(self.minHeap)
        # and then pop until we have k elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


        
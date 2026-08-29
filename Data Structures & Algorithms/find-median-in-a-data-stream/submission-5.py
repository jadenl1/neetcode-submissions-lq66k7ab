import heapq

class MedianFinder:

    def __init__(self):
        self.left = [] # maxheap
        self.right = [] # minheap
        self.median = None

    def addNum(self, num: int) -> None:
        if self.median is None:
            heapq.heappush(self.left, -num)
            self.median = num
            return
        
        if num < self.median:
            heapq.heappush(self.left, -num)
        elif num > self.median:
            heapq.heappush(self.right, num)
        else:
            # push to the smaller heap
            if len(self.left) <= len(self.right):
                heapq.heappush(self.left, -num)
            else:
                heapq.heappush(self.right, num)
        
        # now balance trees
        while len(self.left) > len(self.right):
            heapq.heappush(self.right, -heapq.heappop(self.left))
        
        while len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        
        self.median = self.findMedian()
            

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0]) / 2
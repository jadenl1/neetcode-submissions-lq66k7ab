from collections import deque, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap = []
        cooldowns = deque([]) # q of tups (task, amt, next_avail_cycle)

        for task, freq in Counter(tasks).items():
            heapq.heappush(maxheap, [-freq, task])
        
        cycle = 0
        while maxheap or cooldowns:
            if cooldowns and cooldowns[0][2] == cycle:
                task, amt, next_avail_cycle = cooldowns.popleft()
                heapq.heappush(maxheap, [-amt, task])

            if maxheap:
                freq, task = heapq.heappop(maxheap)
                freq *= -1
                if freq - 1 > 0:
                    cooldowns.append((task, freq - 1, cycle + n + 1))

            cycle += 1
        
        return cycle

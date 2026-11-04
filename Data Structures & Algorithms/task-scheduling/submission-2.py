from collections import deque, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap = []
        cooldowns = deque([]) # q of tups (task, amt, next_avail_cycle)

        for freq in Counter(tasks).values():
            heapq.heappush(maxheap, -freq)
        
        cycle = 0
        while maxheap or cooldowns:
            if cooldowns and cooldowns[0][1] == cycle:
                amt, next_avail_cycle = cooldowns.popleft()
                heapq.heappush(maxheap, -amt)

            if maxheap:
                freq = heapq.heappop(maxheap) * -1

                if freq - 1 > 0:
                    cooldowns.append((freq - 1, cycle + n + 1))

            cycle += 1
        
        return cycle

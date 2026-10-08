import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # set up the graph
        graph = defaultdict(set)

        for source, target, cost in times:
            graph[source].add((cost, target))
        
        # set up dijkstra's
        minheap = [(0, k)]
        distances = {k: 0}
        for i in range(n):
            if i+1 != k:
                distances[i+1] = float('inf')

        while minheap:
            currDist, currNode = heapq.heappop(minheap)

            if currDist > distances[currNode]:
                continue

            for cost, neighbor in graph[currNode]:
                if currDist + cost < distances[neighbor]:
                    distances[neighbor] = currDist + cost
                    heapq.heappush(minheap, (distances[neighbor], neighbor))

        maxDist = -1
        for node, dist in distances.items():
            maxDist = max(maxDist, dist)
            if dist == float('inf'):
                return -1
        
        return maxDist

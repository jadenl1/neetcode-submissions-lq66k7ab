from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # sort all tickets to maintain lexicographical order
        # in reverse so we can pop easily in O(1)
        tickets.sort(reverse=True)

        # len(graph[node]) = out-degree(node)
        for source, target in tickets:      # O(E)
            graph[source].append(target)
        
        path = []
        def dfs(node):
            # iterate over all neighbors
            while graph[node]:
                # delete edge as you explore
                neighbor = graph[node].pop()
                dfs(neighbor)
            
            # once we explored all neighbors, the current node will have 0 out-degree, so add it to path too
            path.append(node)
            return

        dfs('JFK')

        return path[::-1]   # reverse the final solution
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # len(graph[node]) = out-degree(node)
        for source, target in tickets:
            graph[source].append(target)
        
        # sort all neighbors to maintain lexicographical order
        for node, neighbors in graph.items():
            neighbors.sort(reverse=True)

        
        path = []
        def dfs(node):
            if len(graph[node]) == 0: # if there are no outgoing edges
                path.append(node)
                return

            while graph[node]:
                neighbor = graph[node].pop()
                dfs(neighbor)
            
            path.append(node)
            return

        dfs('JFK')

        return path[::-1]
from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        self.visited = set()

        def dfs(root):
            self.visited.add(root)
            for neighbor in graph[root]:
                if neighbor not in self.visited:
                    dfs(neighbor)
            
        components = 0
        for i in range(n):
            if i not in self.visited:
                components += 1
                dfs(i)

        return components
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = []
        components = n

        for i in range(n):
            parent.append(i)

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        def union(x, y):
            parent[find(y)] = find(x)

        for a, b in edges:
            if find(a) == find(b):
                return False
            union(a, b)
            components -= 1
        
        return components == 1
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = []
        for i in range(1, len(edges) + 1):
            parent.append(i)
        
        # parent = [1, 2, 3, 4]
        result = [-1, -1]

        # return root of component that contains x
        def find(x):
            while parent[x-1] != x:
                x = parent[x-1]
            return x

        # make merge components that contain x and y by their roots
        def union(x, y):
            parent[find(y)-1] = find(x) 

        for a, b in edges:
            if find(a) == find(b):
                result = [a, b]
            union(a, b)

        return result
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False  # quick fail for trees
        
        adjMap = defaultdict(list)

        for fromNode, toNode in edges:
            adjMap[fromNode].append(toNode)
            adjMap[toNode].append(fromNode)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            
            if adjMap[node] == []: return True # we are at a leaf
            
            for outgoingNode in adjMap[node]:
                if outgoingNode == parent:
                    continue

                if not dfs(outgoingNode, node):
                    return False

            return True
        
        return dfs(0, -1) and len(visited) == n
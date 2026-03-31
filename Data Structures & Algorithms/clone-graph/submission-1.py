"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graphMap = {}
        
        def search(node):
            if node in graphMap:
                return graphMap[node]
            
            copy = Node(node.val)
            graphMap[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(search(n))
            return copy
        
        return search(node) if node else None
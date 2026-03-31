# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        arr = []
        def dfs(root, maxSeen):
            nonlocal arr

            if not root:
                return
            if root.val >= maxSeen:
                arr.append(root.val)
            newMaxSeen = max(maxSeen, root.val)
            
            dfs(root.left, newMaxSeen)
            dfs(root.right, newMaxSeen)
        
        dfs(root, root.val)
        return len(arr)

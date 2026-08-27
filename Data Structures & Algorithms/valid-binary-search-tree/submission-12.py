# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return (True, float('inf'), float('-inf'))
            
            l, lLo, lHi = dfs(root.left)
            r, rLo, rHi = dfs(root.right)

            isCurrValid = ((root.val > lHi) and (root.val < rLo) and l and r)

            return (isCurrValid, min(lLo, rLo, root.val), max(lHi, rHi, root.val))

        return dfs(root)[0]

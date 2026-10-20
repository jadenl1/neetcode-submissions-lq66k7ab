# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.result = False

        def dfs(node, curr):
            if node:
                if curr + node.val == targetSum and not node.left and not node.right:
                    self.result = True
                    return
                
                dfs(node.left, curr + node.val)
                dfs(node.right, curr + node.val)
        
        dfs(root, 0)

        return self.result

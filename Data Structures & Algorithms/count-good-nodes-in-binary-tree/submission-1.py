# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0

        def dfs(root, greatest):
            if root:
                if root.val >= greatest:
                    self.result += 1
                dfs(root.left, max(greatest, root.val))
                dfs(root.right, max(greatest, root.val))
            
        dfs(root, root.val)
        return self.result
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        if not root:
            return False

        def isSameTree(a, b):
            if not a and b:
                return False
            if not a and not b:
                return True
            if not a:
                return False
            if not b:
                return False

            return a.val == b.val and isSameTree(a.left, b.left) and isSameTree(a.right, b.right)

        if root.val == subRoot.val and isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
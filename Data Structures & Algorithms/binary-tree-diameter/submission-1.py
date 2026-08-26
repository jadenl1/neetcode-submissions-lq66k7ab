# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.best = 0

        def height(root):
            if not root:
                return 0

            leftHeight = height(root.left)
            rightHeight = height(root.right)

            self.best = max(self.best, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)

        height(root)
        return self.best
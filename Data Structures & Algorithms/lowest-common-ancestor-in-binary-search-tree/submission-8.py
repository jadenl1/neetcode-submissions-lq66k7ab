# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # return sets
        # each node, we check if p and q are in both left and right sets
            # if so, we are at the lowest common ancestor
            # if not, add the current node to the set and return
        self.result = None

        def dfs(root):
            if not root:
                return False
            
            left = dfs(root.left)
            right = dfs(root.right)

            curr = root == p or root == q

            if (curr and left) or (curr and right) or (left and right):
                if not self.result:
                    self.result = root
            
            return left or right or root == p or root == q
        
        dfs(root)
        return self.result

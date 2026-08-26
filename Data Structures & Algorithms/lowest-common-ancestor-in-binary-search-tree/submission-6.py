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
                return set()
            
            setL = dfs(root.left)
            setR = dfs(root.right)

            thisSet = setL.union(setR)
            thisSet.add(root)

            if p in thisSet and q in thisSet:
                if not self.result:
                    self.result = root
            
            return thisSet
        
        dfs(root)
        return self.result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        path = []
        def dfs(root, target):
            if not root:
                return False
            
            path.append(root)

            if root.val == target.val:
                return True
            if dfs(root.left, target) or dfs(root.right, target):
                return True
            path.pop()
            return False

        dfs(root, p)
        pathP = list(path)
        
        path.clear()
        dfs(root, q)
        pathQ = list(path)

        for node in pathP:
            print(node.val, end=' ')
        print('')
        for node in pathQ:
            print(node.val, end=' ')
        print('')

        # loop forward until they are different
        i = 0
        while i < len(pathQ) and i < len(pathP) and pathQ[i].val == pathP[i].val:
            i += 1

        print("i: ", i)

        # then we are at an end of some list
        if i >= len(pathQ) or i >= len(pathP):
            return pathP[i-1] # choose champion
        
        if i >= len(pathQ):
            return pathP[i-1]
        if i >= len(pathP):
            return pathQ[i-1]
        
        return pathP[i-1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)

        result = []

        while q:
            currLevel = []
            while q:
                currLevel.append(q.popleft())

            for curr in currLevel:
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
            
            currLevelVals = []
            for node in currLevel:
                if node:
                    currLevelVals.append(node.val)
            if currLevelVals:
                result.append(currLevelVals)

        return result
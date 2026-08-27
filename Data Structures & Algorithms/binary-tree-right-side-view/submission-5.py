# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque()
        q.append(root)

        while q:
            if q[-1]:
                result.append(q[-1].val)

            qLen = len(q)
            for i in range(qLen):
                curr = q.popleft()
                if curr:
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
        
        return result



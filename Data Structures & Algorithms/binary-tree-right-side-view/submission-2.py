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
            level = []
            while q:
                curr = q.popleft()
                if curr:
                    level.append(curr)

            if level and level[-1]:
                result.append(level[-1].val)

            for node in level:
                if node:
                    q.append(node.left)
                    q.append(node.right)
        
        return result



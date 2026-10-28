# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        result = TreeNode(val=preorder[0])
        self.value_map = {}
        for i, val in enumerate(inorder):
            self.value_map[val] = i

        def dfs(l_inorder, r_inorder, root, root_preorder_index):
            root_inorder_index = self.value_map[root.val]


            # left_inorder = curr_inorder[0:root_inorder_index]
            # right_inorder = curr_inorder[root_inorder_index + 1:len(curr_inorder)]

            left_size = root_inorder_index - l_inorder
            right_size = r_inorder - root_inorder_index

            if left_size > 0:
                left_index = root_preorder_index + 1
                left_val = preorder[left_index]

                root.left = TreeNode(val=left_val)
                dfs(root_inorder_index - left_size, root_inorder_index - 1, root.left, left_index)
            
            if right_size > 0:
                right_index = root_preorder_index + left_size + 1
                right_val = preorder[right_index]

                root.right = TreeNode(val=right_val)
                dfs(root_inorder_index + 1, root_inorder_index + right_size, root.right, right_index)

    
        dfs(0, len(inorder)-1, result, 0)

        return result
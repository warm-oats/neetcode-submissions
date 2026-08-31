# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def postorder_dfs(cur_node: TreeNode):
            nonlocal res

            if not cur_node:
                return 0

            left_path = postorder_dfs(cur_node.left)
            right_path = postorder_dfs(cur_node.right)

            res = max(res, left_path + right_path)

            return 1 + max(left_path, right_path)

        postorder_dfs(root)

        return res
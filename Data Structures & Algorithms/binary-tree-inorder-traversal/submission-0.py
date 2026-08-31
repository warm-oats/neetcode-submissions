# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_vals = []

        def inorder_dfs(node: TreeNode):
            if not node:
                return None

            inorder_dfs(node.left)
            inorder_vals.append(node.val)
            inorder_dfs(node.right)

        inorder_dfs(root)

        return inorder_vals
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder_vals = []

        def postorder_dfs(node: TreeNode):
            if not node:
                return None

            postorder_dfs(node.left)
            postorder_dfs(node.right)
            postorder_vals.append(node.val)

        postorder_dfs(root)

        return postorder_vals
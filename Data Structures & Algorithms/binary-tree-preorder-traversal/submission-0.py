# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder_vals = []
        
        def preorder_dfs(node: TreeNode):
            if not node:
                return None

            preorder_vals.append(node.val)
            preorder_dfs(node.left)
            preorder_dfs(node.right)

        preorder_dfs(root)
        
        return preorder_vals

            
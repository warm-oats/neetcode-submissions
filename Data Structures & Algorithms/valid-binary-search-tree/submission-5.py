# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid_tree = True
        
        def dfs(node: TreeNode, lower_limit: int, upper_limit: int):
            if not node:
                return 

            if not lower_limit and not upper_limit:
                dfs(node.left, -math.inf, node.val)
                dfs(node.right, node.val, math.inf)
            else:
                if node.val >= upper_limit or node.val <= lower_limit:
                    nonlocal valid_tree
                    valid_tree = False

                dfs(node.left, lower_limit, min(upper_limit, node.val))
                dfs(node.right, max(lower_limit, node.val), upper_limit)

        dfs(root, None, None)
        return valid_tree

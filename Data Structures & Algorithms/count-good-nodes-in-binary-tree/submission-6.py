# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes_count = 0
        
        def dfs(node: TreeNode, max_path_val: int):
            if not node:
                return None

            node_val = node.val

            if node_val >= max_path_val:
                nonlocal good_nodes_count
                
                good_nodes_count += 1
                max_path_val = node_val

            dfs(node.left, max_path_val)
            dfs(node.right, max_path_val)

        dfs(root, root.val)

        return good_nodes_count
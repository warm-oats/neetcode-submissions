# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def postorder(cur_node, max_path_val):
            if not cur_node:
                return 0

            left_count = postorder(cur_node.left, max(cur_node.val, max_path_val))
            right_count = postorder(cur_node.right, max(cur_node.val, max_path_val))

            valid_node = cur_node.val >= max_path_val

            return valid_node + left_count + right_count

        return postorder(root, root.val)
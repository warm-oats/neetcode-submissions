# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        right_node_stack = []
        curr_node = root

        if not root:
            return not root and not subRoot

        while curr_node:
            if self.dfs(curr_node,subRoot):
                return True

            if curr_node.right:
                right_node_stack.append(curr_node.right)

            if not curr_node.left and right_node_stack:
                curr_node = right_node_stack.pop()
            else:
                curr_node = curr_node.left

        return False

    def dfs(self, root, node_2):
        if not root and not node_2:
            return True

        if (not root and node_2) or (not node_2 and root) or (node_2.val != root.val):
            return False

        return self.dfs(root.left,node_2.left) and self.dfs(root.right,node_2.right)

        return True

            


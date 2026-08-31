# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:     
        tree_stack = []
        curr = root

        if not root and not subRoot:
            return True          
        
        while curr:
            if self.same_tree(curr,subRoot):
                return True

            if curr.right:
                tree_stack.append(curr.right)

            if not curr.left and tree_stack:
                curr = tree_stack.pop()
            else:
                curr = curr.left

        return False
        
    def same_tree(self, root_1, root_2):
        if not root_1 or not root_2:
            if root_1 != root_2:
                return False

            return True

        if root_1.val != root_2.val:
            return False

        left_identical = self.same_tree(root_1.left,root_2.left)
        right_identical = self.same_tree(root_1.right,root_2.right)

        return left_identical and right_identical
        

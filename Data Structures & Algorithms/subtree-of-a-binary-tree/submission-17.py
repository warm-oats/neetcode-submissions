# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subRoot):
            if not root and not subRoot:
                return True

            if not root or not subRoot or root.val != subRoot.val:
                return False

            return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)

        if not root and not subRoot: 
            return True
        
        if not root or not subRoot:
            return False

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return dfs(root, subRoot) or left or right
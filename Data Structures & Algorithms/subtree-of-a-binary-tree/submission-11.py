# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        
        def isSameTree(p: TreeNode, q: TreeNode):
            if not p and not q:
                return True

            if not p and q or p and not q or p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
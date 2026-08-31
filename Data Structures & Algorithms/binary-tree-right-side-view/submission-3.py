# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        order_level_list = []
        res = []

        def dfs(node: TreeNode, depth: int):
            if not node:
                return None

            if (len(order_level_list) - 1) < depth:
                order_level_list.append([node.val])
            else:
                order_level_list[depth].append(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)

        for sublist in order_level_list:
            res.append(sublist[-1])
            
        return res
        

            

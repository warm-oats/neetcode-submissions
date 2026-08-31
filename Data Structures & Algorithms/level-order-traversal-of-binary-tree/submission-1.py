# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order_list = []

        def dfs(node: TreeNode, depth: int):
            if not node:
                return None

            if (len(level_order_list) - 1) < depth:
                new_order_list = [node.val]

                level_order_list.append(new_order_list)
            else:
                level_order_list[depth].append(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return level_order_list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        tree_level_nodes = defaultdict(list)
        res = []

        def dfs(node: TreeNode, depth):
            if not node:
                return None

            if depth > (len(tree_level_nodes) - 1):
                tree_level_nodes[depth] = [node]
            else:
                tree_level_nodes[depth].append(node)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        for sublist in tree_level_nodes.values():
            res.append(sublist[-1].val)

        return res


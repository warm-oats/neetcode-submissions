class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent_list = [i for i in range(len(edges) + 1)]
        res = []

        def find(node: int):
            if node == parent_list[node]:
                return node

            return find(parent_list[node])

        def union(node_1: int, node_2: int):
            par_1, par_2 = find(node_1), find(node_2)

            if par_1 == par_2:
                return False

            parent_list[par_2] = par_1

            return True

        for edge in edges:
            node_1, node_2 = edge[0], edge[1]
            if not union(node_1, node_2):
                res = [node_1, node_2]

        return res
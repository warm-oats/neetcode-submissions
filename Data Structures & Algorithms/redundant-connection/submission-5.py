class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent_list = [i for i in range(len(edges) + 1)]

        def find(node: int):
            if parent_list[node] == node:
                return node

            return find(parent_list[node])

        def union(node_1: int, node_2: int):
            par_1, par_2 = find(node_1), find(node_2)

            if par_1 == par_2:
                return False

            parent_list[par_1] = par_2

            return True

        for edge in edges:
            if not union(edge[0], edge[1]):
                return [edge[0], edge[1]]

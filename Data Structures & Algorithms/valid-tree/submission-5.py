class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        parent_list = defaultdict(list)
        visited = set()

        if not edges: return True

        for node in edges:
            adj_list[node[0]].append(node[1])
            adj_list[node[1]].append(node[0])

            parent_list[node[0]] = -1
            parent_list[node[1]] = -1

        def dfs(node: int, prev_parent: int, parent: int):
            if node in visited:
                if node != prev_parent or node == parent:
                    return False

                return True

            visited.add(node)
            parent_list[node] = parent

            for adjacent in adj_list[node]:
                if not dfs(adjacent, parent_list[node], node):
                    return False

            return True

        return dfs(edges[0][1], parent_list[edges[0][0]], edges[0][1]) and len(visited) == n

            
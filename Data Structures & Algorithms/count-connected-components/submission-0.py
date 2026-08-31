class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj_list = defaultdict(list)
        connected_comps = 0

        for node in edges:
            adj_list[node[0]].append(node[1])
            adj_list[node[1]].append(node[0])

        def dfs(node: int):
            if node in visited:
                return

            visited.add(node)

            for adjacent in adj_list[node]:
                dfs(adjacent)

        for node in range(0, n):
            if node not in visited:
                connected_comps += 1
                dfs(node)

        return connected_comps
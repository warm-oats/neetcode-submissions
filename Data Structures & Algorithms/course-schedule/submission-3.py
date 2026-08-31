class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        visited = set()

        if not prerequisites:
            return True

        for node in prerequisites:
            adj_list[node[0]].append(node[1])

        def dfs(course: int):
            if course in visited:
                return False

            visited.add(course)

            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            adj_list[course] = []

            return True 

        for node in prerequisites:
            if not dfs(node[0]):
                return False

        return True


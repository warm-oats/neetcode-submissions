class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        adj_list = defaultdict(list)
        completed = set()
        res = []

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

            if course not in completed:
                completed.add(course)
                res.append(course)

            return True

        for course in range(0, numCourses):
            if not dfs(course):
                return []

        return res

        

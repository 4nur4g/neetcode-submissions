class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_arr = {i:[] for i in range(numCourses)}
        for course, prq in prerequisites:
            adj_arr[course].append(prq)
        visited = set()
        res = []
        def dfs(crs):
            if crs in res:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for preq in adj_arr[crs]:
                if not dfs(preq):
                    return False
            visited.remove(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
            
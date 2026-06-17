class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_map = {i:[] for i in range(numCourses) } 
        for course, pre_req in prerequisites:
            adj_map[course].append(pre_req)
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if not adj_map[crs]:
                return True
            visited.add(crs)
            for pre_req in adj_map[crs]:
                if not dfs(pre_req):
                    return False
            adj_map[crs] = []
            visited.remove(crs)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        p_visited, a_visited = set(), set()
        DIRS = ((1,0),(-1,0),(0,1), (0,-1))
        def dfs(r,c,visited, prev):
            if not ((r,c) not in visited and 0 <= r < ROWS and 0 <= c < COLS and heights[r][c] >= prev):
                return
            visited.add((r,c))
            for ra, ca in DIRS:
                dfs(r+ra,c+ca, visited, heights[r][c])

        # top and bottom
        for c in range(COLS):
            dfs(0,c,p_visited, float('-inf'))
            dfs(ROWS -1, c,a_visited, float('-inf')) 
        # left and right
        for r in range(ROWS):
            dfs(r,0,p_visited,float('-inf'))
            dfs(r,COLS-1,a_visited,float('-inf'))
        
        # returning intersection
        return list(list(item) for item in p_visited & a_visited)

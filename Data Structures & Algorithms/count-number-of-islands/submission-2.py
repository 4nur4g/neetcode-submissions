class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque([(r,c)])
            visited.add((r,c))

            while q:
                r, c = q.popleft()
                dirs = [(0,1), (0,-1), (-1,0), (1, 0)]
                for ra, ca in dirs:
                    next_r = r + ra
                    next_c = c + ca
                    if next_r in range(rows) and next_c in range(cols) and (next_r, next_c) not in visited and grid[next_r][next_c] == "1":
                        q.append((next_r,next_c))
                        visited.add((next_r,next_c))
                        

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        
        return islands

        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(r,c):
            nonlocal max_area
            q = collections.deque([(r,c)])
            visited.add((r,c))
            area = 0
            while q:
                cell = q.popleft()
                area += 1
                dirs = ((1,0), (-1,0), (0,1), (0,-1))
                for ra, ca in dirs:
                    cr, cc = cell
                    nr, nc = cr + ra, cc + ca
                    if (nr, nc) not in visited and 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        visited.add((nr,nc))
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(bfs(r,c), max_area)
        return max_area

                    

            
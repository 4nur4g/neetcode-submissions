class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        dimen_row = len(grid)
        dimen_col = len(grid[0])
        visited = set()
        count = 0
        def bfs(r,c,visited):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                curr = q.popleft()
                rc,cc = curr
                dirs = [(0,-1),(0,1),(-1,0),(1,0)]
                for dr, dc in dirs:
                    nr, nc = rc + dr, cc + dc
                    if nr in range(dimen_row) and nc in range(dimen_col) and grid[nr][nc] == '1' and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))
        

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c,visited)
                    count += 1
        return count

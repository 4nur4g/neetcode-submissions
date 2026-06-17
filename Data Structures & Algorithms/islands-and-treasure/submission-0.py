class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(r,c):
            q = collections.deque()
            visited = set()
            q.append((r,c))
            visited.add((r,c))
            layer = 0
            while q:
                level_size = len(q)
                for _ in range(level_size):
                    move = [(-1,0), (1,0), (0,-1), (0,1)]
                    cr, cc = q.popleft()
                    for ra, ca in move:
                        nr, nc = cr + ra, cc + ca
                        if nr in range(len(grid)) and nc in range(len(grid[0])) and (nr,nc) not in visited and grid[nr][nc] != -1:
                            if grid[nr][nc] not in [-1,0]:
                                grid[nr][nc] = min(layer+1,grid[nr][nc])
                            visited.add((nr,nc))
                            q.append((nr,nc))
                layer += 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    bfs(r,c)




        
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs():
            if not grid:
                return
            visited = set()
            q = collections.deque()
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 0:
                        q.append((r,c))
                        visited.add((r,c))
            dist = 0
            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    dirs = [(0,-1), (0,1), (-1,0),(1,0)]
                    for ra, ca in dirs:
                        nr = r + ra
                        nc = c + ca
                        if (nr,nc) not in visited and nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] != -1:
                            grid[nr][nc] = dist + 1
                            visited.add((nr,nc))
                            q.append((nr,nc))
                dist += 1
        bfs()
                            






        
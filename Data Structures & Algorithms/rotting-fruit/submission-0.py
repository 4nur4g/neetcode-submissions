class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs():
            q = collections.deque()
            visited = set()
            fresh_fruits = 0
            new_rotten_fruits = 0
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 2:
                        q.append((r,c))
                        visited.add((r,c))
                    if grid[r][c] == 1:
                        fresh_fruits += 1
            if fresh_fruits == 0:
                return 0

            layer = 0
            while q:
                for _ in range(len(q)):
                    cr, cc = q.popleft()
                    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
                    for ra, ca in dirs:
                        nr, nc = cr + ra, cc + ca
                        if (nr,nc) not in visited and nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == 1:
                            visited.add((nr,nc))
                            q.append((nr,nc))
                            new_rotten_fruits += 1
                layer += 1
                if new_rotten_fruits == fresh_fruits:
                    return layer
            
            return layer if new_rotten_fruits == fresh_fruits else -1
        return bfs()

        
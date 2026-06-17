class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # initially
        rotten = []
        fresh = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten.append((r,c))
        time = 0        
        q = collections.deque(rotten)
        dirs = ((1,0), (-1,0), (0,1), (0,-1))
        visited = set(rotten)
        while q and fresh > 0:
            for _ in range(len(q)): 
                row, col = q.popleft()
                for ra, ca in dirs:
                    r = row + ra
                    c = col + ca
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r,c) not in visited:
                        visited.add((r,c))
                        fresh -= 1
                        q.append((r,c))
            time += 1

        return time if fresh == 0 else -1


        

        
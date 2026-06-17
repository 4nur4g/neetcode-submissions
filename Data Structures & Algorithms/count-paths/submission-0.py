class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # BFS

        ROWS, COLS = m, n 
        # q = deque([(0,0)])
        # res = 0
        # while q:
        #     for r in range(len(q)):
        #         cr, cc = q.popleft()
        #         if cr == ROWS - 1 and cc == COLS - 1:
        #             res += 1
        #         dirs = [(1,0),(0,1)]
        #         for r_add, c_add in dirs:
        #             nr, nc = cr + r_add, cc + c_add
        #             if nr in range(ROWS) and nc in range(COLS):
        #                 q.append((nr,nc))
                    
        # return res

        # DFS

        visited = set()
        cache = {} 
        def dfs(r,c):

            if (r,c) in cache:
                return cache[(r,c)]
                
            if (r == ROWS -1) and (c == COLS -1):
                return 1
            dirs = [(1,0),(0,1)]

            count = 0

            for r_add, c_add in dirs:
                nr, nc = r + r_add, c + c_add
                if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    count += dfs(nr, nc)
                    visited.remove((nr,nc))

            cache[(r,c)] = count           
            return count

        return dfs(0,0)
            



                        
        
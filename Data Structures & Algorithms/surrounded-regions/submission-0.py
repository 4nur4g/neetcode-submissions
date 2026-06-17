class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(r,c):
            if (r,c) in visited or r not in range(ROWS) or c not in range(COLS) or board[r][c] != "O":
                return
            visited.add((r,c))
            board[r][c] = '#'
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            for ra, ca in dirs:
                dfs(r+ra, c+ca)
            visited.remove((r,c))
        # Looping borders, left, right
        for r in range(ROWS):
            # left
            dfs(r,0)
            # right
            dfs(r,COLS-1)
        for c in range(COLS):
            # top
            dfs(0,c)
            # bottom
            dfs(ROWS-1,c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"

        
        
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        inc_diag = set()
        dec_diag = set()
        cols = set()
        res = []
        def backtrack(r):
            if r >= n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                current_dec_diag = r-c
                current_inc_diag = r + c
                if c in cols or current_dec_diag in dec_diag or current_inc_diag in inc_diag:
                    continue
                cols.add(c)
                inc_diag.add(current_inc_diag)
                dec_diag.add(current_dec_diag)
                board[r][c] = "Q"

                backtrack(r+1)

                board[r][c] = "."
                cols.remove(c)
                inc_diag.remove(current_inc_diag)
                dec_diag.remove(current_dec_diag)
        backtrack(0)
        return res



            
            
        
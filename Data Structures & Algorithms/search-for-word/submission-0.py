class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w,h = len(board[0]), len(board)
        track = set()

        def backtrack(r,c,i):
            if i >= len(word):
                return True
            if (r < 0 or c < 0 or r >= h or c >= w
                or (r,c) in track or word[i] != board[r][c]):
                return False
            track.add((r,c))
            res = (backtrack(r+1, c, i+1) or
                backtrack(r, c+1, i+1) or 
                backtrack(r-1, c, i+1) or
                backtrack(r, c-1, i+1))
            track.remove((r,c))
            return res

        for r in range(h):
            for c in range(w):
                if backtrack(r,c,0):
                    return True
        return False

        
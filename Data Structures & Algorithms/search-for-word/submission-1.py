class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cols, rows = len(board[0]), len(board)
        visited = set()
        formed_word = ""
        def backtrack(r,c,char_ind):
            nonlocal formed_word
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or board[r][c] != word[char_ind]:
                return False
            if char_ind == len(word) - 1:
                return True
            if board[r][c] == word[char_ind]:
                char_ind += 1
            visited.add((r,c))
            left = backtrack(r,c-1, char_ind)    
            right = backtrack(r, c+1, char_ind)
            top = backtrack(r + 1, c, char_ind)
            bottom = backtrack(r - 1, c, char_ind)
            visited.remove((r,c))
            return left or right or top or bottom
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        
        return False


        
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, box = [collections.defaultdict(set) for _ in range(3)]
        for r in range(len(board)):
            for c in range(len(board[r])):
                num = board[r][c]
                if num == ".":
                    continue
                    
                if num in row[r]:
                    return False
                if num in col[c]:
                    return False

                box_x = r // 3
                box_y = c // 3
                if num in box[(box_x,box_y)]:
                    return False
                row[r].add(num)
                col[c].add(num)
                box[(box_x,box_y)].add(num)
        return True

        
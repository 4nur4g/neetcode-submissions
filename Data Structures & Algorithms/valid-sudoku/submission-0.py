class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tempSet = set()
        # Checking rows
        for row in board:
            for number in row:
                if number in tempSet:
                    return False
                if number != '.':
                    tempSet.add(number)
            tempSet.clear()
        # Checking columns
        col = 0
        while col < 9:
            for row in range(9):
                if board[row][col] in tempSet:
                    return False
                if board[row][col] != '.':
                    tempSet.add(board[row][col])
            tempSet.clear()
            col += 1
        # Checking 3*3 boxes
        boxMap = collections.defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] in boxMap[(row//3,col//3)]:
                    return False
                if board[row][col] != '.':
                    boxMap[(row//3,col//3)].add(board[row][col])
        return True



        
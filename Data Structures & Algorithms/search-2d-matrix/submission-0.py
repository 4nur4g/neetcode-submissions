class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        top = 0
        bottom = len(matrix) - 1
        middle = None
        while top <= bottom:
            middle = (top + bottom)//2
            if target > matrix[middle][-1]:
                top = middle + 1
            elif target < matrix[middle][0]:
                bottom = middle - 1
            else:
                break
        if top > bottom:
            return False
        row = matrix[middle]
        start = 0
        end = len(row) - 1
        while start <= end:
            middle = (start + end) // 2
            if row[middle] == target:
                return True
            if row[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
        return False
        
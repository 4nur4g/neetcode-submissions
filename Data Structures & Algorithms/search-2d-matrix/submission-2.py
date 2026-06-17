class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix:
            if r[0] <= target <= r[-1]:
                left = 0
                right = len(r) - 1
                while left <= right:
                    m = left + (right - left)//2
                    if r[m] == target:
                        return True
                    elif r[m] > target:
                        right = m - 1
                    else:
                        left = m + 1
        return False
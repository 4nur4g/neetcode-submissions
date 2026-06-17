from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0

        # Inclusive boundaries:
        # left[i]  = first index you can include on the left
        # right[i] = first index you can include on the right
        left = [0] * n
        right = [n - 1] * n

        # Monotonic stack for left (indices with increasing heights)
        stack = []
        for i in range(n):
            # pop while current bar is <= stack top (so we get strictly smaller)
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            # If stack empty, we can extend to 0; else to stack[-1] + 1
            left[i] = (stack[-1] + 1) if stack else 0
            stack.append(i)

        # Monotonic stack for right (indices with increasing heights)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            # If stack empty, we can extend to n-1; else to stack[-1] - 1
            right[i] = (stack[-1] - 1) if stack else (n - 1)
            stack.append(i)

        # Compute max area
        res = 0
        for i in range(n):
            width = right[i] - left[i] + 1
            res = max(res, heights[i] * width)

        return res
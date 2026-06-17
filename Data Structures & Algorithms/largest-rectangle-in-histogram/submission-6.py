from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []            # stores indices, heights strictly increasing
        max_area = 0
        n = len(heights)

        for i in range(n + 1):  # iterate one extra step with sentinel height 0
            cur = heights[i] if i < n else 0
            # flush taller bars
            while stack and heights[stack[-1]] > cur:
                h = heights[stack.pop()]
                left_smaller = stack[-1] if stack else -1  # exclusive
                width = i - left_smaller - 1
                max_area = max(max_area, h * width)
            stack.append(i)

        return max_area
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stack to store (index, height)
        maxArea = 0
        
        for index, item in enumerate(heights):
            while stack and stack[-1][1] > item:
                poppedIndex, height = stack.pop()
                width = index if not stack else index - stack[-1][0] - 1
                maxArea = max(maxArea, width * height)
            stack.append((index, item))
        while stack:
            poppedIndex, height = stack.pop()
            width = len(heights) if not stack else len(heights) - stack[-1][0] - 1
            maxArea = max(maxArea, width * height)
        
        return maxArea
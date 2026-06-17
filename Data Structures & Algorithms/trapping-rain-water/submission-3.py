class Solution:
    def trap(self, height: List[int]) -> int:
        max_to_left, max_to_right = [0] * len(height), [0] * len(height)
        total_area = 0
        for i in range(1,len(height)):
            max_to_left[i] = max(height[i-1],max_to_left[i-1])
        for i in range(len(height)-2,-1,-1):
            max_to_right[i] = max(height[i+1],max_to_right[i+1])
        for i,h in enumerate(height):
            area = min(max_to_left[i],max_to_right[i]) - h
            if area > 0:
                total_area += area
        return total_area


        
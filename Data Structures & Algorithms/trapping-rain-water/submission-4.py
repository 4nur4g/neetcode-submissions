class Solution:
    def trap(self, height: List[int]) -> int:
        look_right, look_left = [0] * len(height), [0] * len(height)
        temp = float('-inf')
        # Look left
        for ind, h in enumerate(height):
            look_left[ind] = max(temp,look_left[ind-1] if ind > 0 else 0) 
            temp = max(h,temp)
        temp = float('-inf')
        # Look right
        for i in range(len(height)-1,-1,-1):
            look_right[i] = max(temp,look_right[(i+1)] if i < len(height) - 1 else 0) 
            temp = max(height[i], temp)
        res = 0
        for ind, h in enumerate(height):
            current = min(look_left[ind],look_right[ind]) - h
            res += current if current > 0 else 0
        return res






        
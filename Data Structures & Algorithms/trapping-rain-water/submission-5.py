class Solution:
    def trap(self, height: List[int]) -> int:
        look_right, look_left = [0] * len(height), [0] * len(height)
        temp = 0
        # Look left
        for ind, h in enumerate(height):
            look_left[ind] = temp
            temp = max(h,temp)
        temp = 0
        # Look right
        for i in range(len(height)-1,-1,-1):
            look_right[i] = temp
            temp = max(height[i], temp)
        res = 0
        for ind, h in enumerate(height):
            # Gotcha, be careful, we're subracting height! Can become negative
            current = min(look_left[ind],look_right[ind]) - h
            res += current if current > 0 else 0
        return res






        
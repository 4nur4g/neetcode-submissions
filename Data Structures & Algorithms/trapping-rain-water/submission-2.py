class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for i,h in enumerate(height):
            maxLeft = 0
            maxRight = 0
            left = i-1
            right = i+1

            while left >= 0:
                maxLeft = max(maxLeft, height[left])
                left -= 1
            while right < len(height):
                maxRight = max(maxRight, height[right])
                right += 1
            current = min(maxLeft, maxRight) - h
            if current > 0:
                total += current
        return total
            



                
        
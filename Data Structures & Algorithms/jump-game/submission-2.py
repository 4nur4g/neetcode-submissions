from functools import lru_cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(i):
            if i == len(nums) - 1:
                return True
            if i >= len(nums):
                return False
            if nums[i] == 0:
                return False
            
            for j in range(1,nums[i]+1):
                if dfs(i+j):
                    return True
            return False
        return dfs(0)
        
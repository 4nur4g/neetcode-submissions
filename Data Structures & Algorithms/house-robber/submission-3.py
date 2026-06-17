class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(nums):
                return 0
            amount = max(nums[i] + dfs(i+2), dfs(i+1))
            cache[i] = amount
            return cache[i]
        return dfs(0)
        
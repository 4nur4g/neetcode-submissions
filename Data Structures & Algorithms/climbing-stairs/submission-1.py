class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(prev_sum):
            res = 0
            if prev_sum == n:
                return 1
            if prev_sum > n: 
                return 0
            if prev_sum in cache:
                return cache[prev_sum]
            res += dfs(prev_sum + 1) + dfs(prev_sum + 2)
            cache[prev_sum] = res
            return res
        return dfs(0)
        
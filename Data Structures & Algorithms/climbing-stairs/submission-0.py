class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(prev_sum):
            res = 0
            if prev_sum == n:
                return 1
            if prev_sum > n: 
                return 0
            res += dfs(prev_sum + 1) + dfs(prev_sum + 2)
            return res
        return dfs(0)
        
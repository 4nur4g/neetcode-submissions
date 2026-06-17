class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            # taking one step
            one = dfs(i+1) if not (i + 1) in cache else cache[i+1]
            two = dfs(i+2) if not (i + 2) in cache else cache[i+2]
            cache[i] = one + two
            return cache[i]

        return dfs(0)

        
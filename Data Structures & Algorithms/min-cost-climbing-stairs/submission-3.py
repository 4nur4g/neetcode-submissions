class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        SIZE = len(cost)
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= SIZE:
                return 0
            cost_from_i = cost[i] + min(dfs(i+1),dfs(i+2))
            cache[i] = cost_from_i
            return cache[i]
        return min(dfs(0),dfs(1))
        
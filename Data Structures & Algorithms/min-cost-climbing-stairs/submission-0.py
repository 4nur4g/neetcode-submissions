class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(step):
            if step >= len(cost):
                return 0
            if step in memo:
                return memo[step]
            current_cost = cost[step] + min(dfs(step + 1), dfs(step + 2))
            memo[step] = current_cost
            return current_cost
        return min(dfs(0), dfs(1))
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = float("+inf")
        SIZE = len(cost)
        temp_cost = 0
        def dfs(i):
            nonlocal temp_cost
            nonlocal min_cost
            if i > SIZE:
                return 
            if i == SIZE:
                min_cost = min(min_cost,temp_cost)
                return
            temp_cost += cost[i]
            dfs(i+1)
            dfs(i+2)

            temp_cost -= cost[i]
        dfs(0)
        dfs(1)
        return min_cost
        
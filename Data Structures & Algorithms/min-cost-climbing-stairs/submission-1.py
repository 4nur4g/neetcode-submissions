class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memo = {}
        # def dfs(step):
        #     if step >= len(cost):
        #         return 0
        #     if step in memo:
        #         return memo[step]
        #     current_cost = cost[step] + min(dfs(step + 1), dfs(step + 2))
        #     memo[step] = current_cost
        #     return current_cost
        # return min(dfs(0), dfs(1))

        cost.append(0)

        for i in range(len(cost)-3,-1,-1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        
        return min(cost[0],cost[1])
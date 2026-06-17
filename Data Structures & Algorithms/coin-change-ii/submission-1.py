class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i,total):
            if (i,total) in cache:
                return cache[(i,total)]
            count = 0
            if i >= len(coins) or total > amount:
                return 0
            if total == amount:
                return 1
            for j in range(i,len(coins)):
                count += dfs(j,total+coins[j])
            cache[(i,total)] = count
            return count
        return dfs(0,0)
        
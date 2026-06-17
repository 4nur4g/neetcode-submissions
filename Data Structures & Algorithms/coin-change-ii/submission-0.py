class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i,total):
            if (i,total) in cache:
                return cache[(i,total)]
            ans = 0
            if i >= len(coins) or total > amount:
                return 0
            if total == amount:
                return 1
            for j in range(i,len(coins)):
                ans += dfs(j,total+coins[j])
            cache[(i,total)] = ans
            return ans
        return dfs(0,0)
        
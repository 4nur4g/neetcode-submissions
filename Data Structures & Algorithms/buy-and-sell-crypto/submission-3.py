class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Imagine a graph plot
        # Time runs positive, not negatively
        if len(prices) < 2:
            return 0
        l = 0
        r = 1
        res = 0
        while l < len(prices) and r < len(prices):
            diff = prices[r] - prices[l]
            res = max(res,diff)
            if diff < 0:
                l = r
                r = r + 1
            else:
                r += 1
        return res

        
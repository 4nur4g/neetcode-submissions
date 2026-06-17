class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        p1, p2 = 0, 1
        res = 0
        while p2 < len(prices):
            if prices[p2] < prices[p1]:
                p1 = p2
                p2 += 1
                continue
            diff = prices[p2] - prices[p1]
            res = max(diff,res)
            p2 += 1
        return res


        
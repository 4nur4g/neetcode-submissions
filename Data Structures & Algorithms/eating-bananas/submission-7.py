class Solution:
    @staticmethod
    def get_time_taken(k, piles):
        res = 0
        for pile in piles:
            res += math.ceil(pile/k)
        return res

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = float('inf')
        while l <= r:
            m = l + (r - l) // 2
            time = self.get_time_taken(m, piles)
            if time > h:
                l = m + 1
            else:
                res = min(res,m )
                r = m - 1 
        return res
            
        
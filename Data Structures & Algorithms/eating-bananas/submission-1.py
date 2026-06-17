class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        ans = max(piles) #Max rate
        while start <= end:
            m = (start + end)//2
            timeTaken = 0
            for pile in piles:
                timeTaken += math.ceil(pile/m)
            if timeTaken > h:
                start = m + 1
            else:
                ans = min(ans,m)
                end = m - 1
               
        return ans


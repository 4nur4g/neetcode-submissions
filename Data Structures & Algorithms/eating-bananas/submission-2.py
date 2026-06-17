class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        ans = max(piles) #Max rate
        while start <= end:
            k = (start + end)//2
            timeTaken = 0
            for pile in piles:
                timeTaken += math.ceil(pile/k)
            if timeTaken > h:
                start = k + 1
            else:
                ans = min(ans,k)
                end = k - 1
               
        return ans


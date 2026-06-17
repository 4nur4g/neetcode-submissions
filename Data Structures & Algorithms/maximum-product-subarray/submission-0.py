class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Keep track of max and min
        maxim, minim = 1,1
        res = max(nums)

        for n in nums:
            if n == 0:
                maxim, minim = 1,1
                continue
            tmp = maxim
            # Notice, n is involved here everywhere
            maxim = max(minim * n, maxim * n, n)
            minim = min(minim * n, tmp * n, n)

            res = max(res, maxim)

        return res
            
                

        
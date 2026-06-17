class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track = set(nums)
        res = 0
        for n in nums:
            count = 1
            t = n
            if n - 1 in track:
                continue
            while t+1 in track:
                count += 1
                t += 1 
            res = max(count,res)
        return res

        
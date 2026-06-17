class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for ind,n in enumerate(nums):
            if ind > 0 and n == nums[ind-1]:
                continue
            l = ind + 1
            r = len(nums) - 1
            while l < r:
                t = n + nums[l] + nums[r]
                if t > 0:
                    r -= 1
                elif t < 0:
                    l += 1
                else:
                    res.append([nums[ind],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while r > l and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res






        
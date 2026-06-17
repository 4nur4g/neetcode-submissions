class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = float('inf')
        while l <= r:
            m = (l+r)//2
            if nums[l] <= nums[r]:
                return min(nums[l],minimum)
            minimum = min(minimum,nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return minimum
                
        
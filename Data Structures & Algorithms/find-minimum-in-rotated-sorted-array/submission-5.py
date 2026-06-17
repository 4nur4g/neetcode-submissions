class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            m = l + (r-l) // 2
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m
        return -1
        
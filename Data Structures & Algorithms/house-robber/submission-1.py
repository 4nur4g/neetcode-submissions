class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [nums[0],max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            maximum = max(nums[i] + dp[0], dp[1])
            dp[0] = dp[1]
            dp[1] = maximum
        return dp[1]

        
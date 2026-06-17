class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        dp1 = [0,0]
        dp2 = [0,0]

        # considering starting index, leaving last one
        for i in range(len(nums)-1):
            curr_max = max(dp1[1], nums[i] + dp1[0])
            dp1[0] = dp1[1]
            dp1[1] = curr_max
        # Leaving starting index, including last one
        for i in range(1,len(nums)):
            curr_max = max(dp2[1], nums[i] + dp2[0])
            dp2[0] = dp2[1]
            dp2[1] = curr_max
        
        return max(dp1[1], dp2[1])



        
        
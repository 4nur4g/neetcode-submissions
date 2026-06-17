class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            global_max = max(curr_sum,global_max)

        return global_max
        
        
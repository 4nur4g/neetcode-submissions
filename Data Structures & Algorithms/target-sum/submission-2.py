class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i,curr_sum):
            if (i,curr_sum) in cache:
                return cache[(i,curr_sum)]
            if curr_sum == target and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            count = 0
            count += dfs(i+1,curr_sum + nums[i])
            count += dfs(i+1,curr_sum - nums[i])
            cache[(i,curr_sum)] = count
            return count
        return dfs(0,0)


        
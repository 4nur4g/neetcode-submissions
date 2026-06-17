class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        to_find = sum(nums)//2
        sum_set = set([0])
        for i in range(len(nums)-1,-1,-1):
            next_sum_set = set()
            for s in sum_set:
                if s == to_find:
                    return True
                next_sum_set.add(s+nums[i])
                next_sum_set.add(s)
            sum_set = next_sum_set

        return True if to_find in sum_set else False

        
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def backtrack(i):
            if sum(sub) == target:
                res.append(sub.copy())
                return
            if sum(sub) > target or i >= len(nums):
                return
            
            # choosing
            sub.append(nums[i])
            backtrack(i)

            # not choosing
            sub.pop()
            backtrack(i+1)
        backtrack(0)
        return res


        
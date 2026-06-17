class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sub, res = [], []
        size = len(nums)
        def backtrack(i):
            if i >= size:
                res.append(sub.copy())
                return
            # make selection
            sub.append(nums[i]) 
            backtrack(i+1)

            # don't make selection
            sub.pop()
            
            # follow up branching should skip duplicates

            j = i + 1

            while j < size and nums[j] == nums[i]:
                j += 1

            backtrack(j)
        backtrack(0)
        return res
                
        
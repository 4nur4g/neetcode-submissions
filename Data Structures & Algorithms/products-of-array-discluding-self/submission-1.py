class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mul, right_mul = [0] * len(nums), [0] * len(nums)
        left_mul[0] = right_mul[len(nums)-1] = 1
        res = []

        for i in range(1,len(nums)):
            left_mul[i] = nums[i-1]*left_mul[i-1]
        for i in range(len(nums)-2,-1,-1):
            right_mul[i] = nums[i+1]*right_mul[i+1]
        for i,_ in enumerate(nums):
            res.append(left_mul[i]*right_mul[i])
        return res
        


        
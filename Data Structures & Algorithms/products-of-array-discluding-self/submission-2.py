class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = collections.deque(), collections.deque()
        t = 1
        for n in nums:
            left.append(t)
            t = t*n
        t = 1
        for i in range(len(nums)-1,-1,-1):
            right.appendleft(t)
            t = nums[i]*t
        res = []
        for i in range(len(nums)):
            p = left[i] * right[i]
            res.append(p)
        return res





        
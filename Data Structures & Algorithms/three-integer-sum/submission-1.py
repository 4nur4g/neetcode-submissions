class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for index,num in enumerate(nums):
            if index != 0 and nums[index-1] == num:
                continue
            reqSum = -num
            left = index + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == reqSum:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    right -= 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                elif nums[left] + nums[right] < reqSum:
                    left += 1
                else:
                    right -= 1
        return ans


        
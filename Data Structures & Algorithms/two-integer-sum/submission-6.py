class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for ind, n in enumerate(nums):
            diff = target - n
            if diff in temp:
                return [temp[diff],ind]
            temp[n] = ind
        return []
        
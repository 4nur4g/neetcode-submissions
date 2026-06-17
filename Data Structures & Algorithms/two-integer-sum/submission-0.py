class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # val -> index
        valToInd = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in valToInd:
                return [valToInd[diff],index]
            valToInd[num] = index


        
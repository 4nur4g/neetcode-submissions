class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index_list = [
            (num, index) for index,num in enumerate(nums)
        ]

        nums_index_list.sort()
        
        i = 0
        j = len(nums) - 1

        while i < j:
            total = nums_index_list[i][0] + nums_index_list[j][0]
            if total == target:
                return [min(nums_index_list[i][1], nums_index_list[j][1]), max(nums_index_list[i][1], nums_index_list[j][1])]
            if total < target:
                i += 1
            else: 
                j -= 1
        
        return []
        
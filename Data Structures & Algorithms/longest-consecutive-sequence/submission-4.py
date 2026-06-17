class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ordered = sorted(set(nums))
        maximum = 1
        current_max = 1

        for i in range(1,len(ordered)):
            if ordered[i] == ordered[i-1] + 1:
                current_max += 1
            else:
                current_max = 1
            maximum = max(current_max,maximum)
        return maximum
        

            

        